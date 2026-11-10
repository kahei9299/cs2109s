import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import numpy as np

# Generate sine wave data
def generate_sine_wave(num_time_steps):
    time_steps = torch.linspace(0, 4 * np.pi, num_time_steps)
    data = torch.sin(time_steps)
    return data

def create_sequences(sine_wave, seq_length):
    sequences = []
    labels = []
    for i in range(len(sine_wave) - seq_length):
        sequences.append(sine_wave[i:i+seq_length])
        labels.append(sine_wave[i+seq_length])
    return torch.stack(sequences), torch.stack(labels)

num_time_steps = 1000
sine_wave_data = generate_sine_wave(num_time_steps)
seq_length = 20
sequences, labels = create_sequences(sine_wave_data, seq_length)
sequences = sequences.unsqueeze(-1)

train_size = int(len(sequences) * 0.5)
train_seqs = sequences[:train_size]
train_labels = labels[:train_size]
test_seqs = sequences[train_size:]
test_labels = labels[train_size:]

# Positional Encoding
class PositionalEncoding(nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        batch_size, seq_len, d = x.shape
        pos = torch.arange(seq_len, dtype=torch.float32, device=x.device).unsqueeze(1)
        k = torch.arange(0, d, 2, dtype=torch.float32, device=x.device)
        div_term = 10000.0 ** (k / d)
        pe = torch.zeros(seq_len, d, device=x.device)
        pe[:, 0::2] = torch.sin(pos / div_term)
        pe[:, 1::2] = torch.cos(pos / div_term)
        return x + pe

# Transformer WITH positional encoding
class TransformerNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.embedding = nn.Linear(input_size, hidden_size)
        self.positional_encoder = PositionalEncoding()
        encoder_layer = nn.TransformerEncoderLayer(d_model=hidden_size, dim_feedforward=hidden_size, nhead=1, batch_first=True)
        self.transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers=1)
        self.fc_out = nn.Linear(hidden_size, output_size)
    def forward(self, x):
        x = self.embedding(x)
        x = self.positional_encoder(x)
        x = self.transformer_encoder(x)
        x = x.mean(dim=1)
        return self.fc_out(x)

# Transformer WITHOUT positional encoding
class TransformerNN_NoPE(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.embedding = nn.Linear(input_size, hidden_size)
        encoder_layer = nn.TransformerEncoderLayer(d_model=hidden_size, dim_feedforward=hidden_size, nhead=1, batch_first=True)
        self.transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers=1)
        self.fc_out = nn.Linear(hidden_size, output_size)
    def forward(self, x):
        x = self.embedding(x)
        x = self.transformer_encoder(x)
        x = x.mean(dim=1)
        return self.fc_out(x)

def train_and_eval(model, name):
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    num_epochs = 200
    for epoch in range(num_epochs):
        model.train()
        optimizer.zero_grad()
        outputs = model(train_seqs)
        loss = criterion(outputs.squeeze(), train_labels.squeeze())
        loss.backward()
        optimizer.step()
        if (epoch + 1) % 50 == 0:
            print(f"[{name}] Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.6f}")
    model.eval()
    with torch.no_grad():
        y_pred = model(test_seqs).squeeze()
        y_true = test_labels.squeeze()
    print(f"[{name}] Test MSE: {criterion(y_pred, y_true).item():.6f}")
    return y_pred.numpy(), y_true.numpy()

# Train both models
print("=== Training WITH Positional Encoding ===")
model_pe = TransformerNN(1, 50, 1)
pred_pe, true_vals = train_and_eval(model_pe, "With PE")

print("\n=== Training WITHOUT Positional Encoding ===")
model_no_pe = TransformerNN_NoPE(1, 50, 1)
pred_no_pe, _ = train_and_eval(model_no_pe, "No PE")

# Plot both
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

ax1.plot(true_vals, label="Actual")
ax1.plot(pred_pe, label="Predicted")
ax1.set_title("Transformer WITH Positional Encoding")
ax1.legend()

ax2.plot(true_vals, label="Actual")
ax2.plot(pred_no_pe, label="Predicted")
ax2.set_title("Transformer WITHOUT Positional Encoding")
ax2.legend()

plt.tight_layout()
plt.savefig("task43_plots.png", dpi=150)
print("\nPlots saved to task43_plots.png")
plt.show()
