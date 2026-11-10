
_ML_MODEL = None

def _get_ml_model():
    global _ML_MODEL
    if _ML_MODEL is None:
        _ML_MODEL = get_model()
    return _ML_MODEL

# ── Compact state for A* search ──────────────────────────────

_DIR = {Action.UP: (0, -1), Action.DOWN: (0, 1),
        Action.LEFT: (-1, 0), Action.RIGHT: (1, 0)}
_MOVES = (Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT)
_ADJ4 = ((0, -1), (0, 1), (-1, 0), (1, 0))

_Static = namedtuple("_Static", "walls lava exit w h cost tlim")
_S = namedtuple("_S",
    "pos hp nk sc turn gems doors boxes kg co spu hpu ppu aspd ashd aph win lose")


def _extract(gs):
    w, h = gs.width, gs.height
    walls = set(); lava = set(); ex = None
    ap = None; ahp = 5; ank = 0
    aspd = []; ashd = []; aph = []
    gems = set(); doors = set(); boxes = set()
    kg = set(); co = set(); spu = set(); hpu = set(); ppu = set()
    for x in range(w):
        for y in range(h):
            for e in gs.grid[x][y]:
                p = (x, y)
                t = type(e)
                if t is AgentEntity:
                    ap = p; ahp = e.health.current_health
                    ank = sum(1 for i in e.inventory_list if isinstance(i, KeyEntity))
                    for ef in e.status_list:
                        if isinstance(ef, SpeedPowerUpEntity): aspd.append(ef.time_limit.amount)
                        elif isinstance(ef, ShieldPowerUpEntity): ashd.append(ef.usage_limit.amount)
                        elif isinstance(ef, PhasingPowerUpEntity): aph.append(ef.time_limit.amount)
                elif t is WallEntity: walls.add(p)
                elif t is LavaEntity: lava.add(p)
                elif t is ExitEntity: ex = p
                elif t is GemEntity: gems.add(p)
                elif t is LockedDoorEntity: doors.add(p)
                elif t is BoxEntity: boxes.add(p)
                elif t is KeyEntity: kg.add(p)
                elif t is CoinEntity: co.add(p)
                elif t is SpeedPowerUpEntity: spu.add(p)
                elif t is ShieldPowerUpEntity: hpu.add(p)
                elif t is PhasingPowerUpEntity: ppu.add(p)
    static = _Static(frozenset(walls), frozenset(lava), ex, w, h, gs.step_cost, gs.turn_limit)
    s0 = _S(ap, ahp, ank, gs.score, gs.turn,
            frozenset(gems), frozenset(doors), frozenset(boxes),
            frozenset(kg), frozenset(co),
            frozenset(spu), frozenset(hpu), frozenset(ppu),
            tuple(sorted(aspd)), tuple(sorted(ashd)), tuple(sorted(aph)),
            False, False)
    return static, s0


def _skey(s):
    return (s.pos, s.hp, s.nk, s.gems, s.doors, s.boxes,
            s.kg, s.spu, s.hpu, s.ppu, s.aspd, s.ashd, s.aph)


def _skey_co(s):
    return (s.pos, s.hp, s.nk, s.gems, s.doors, s.boxes,
            s.kg, s.co, s.spu, s.hpu, s.ppu, s.aspd, s.ashd, s.aph)


def _sim(s, act, st):
    pos, hp, nk, sc = s.pos, s.hp, s.nk, s.sc
    gems, doors, boxes = s.gems, s.doors, s.boxes
    kg, co = s.kg, s.co
    spu, hpu, ppu = s.spu, s.hpu, s.ppu
    aspd, ashd, aph = list(s.aspd), list(s.ashd), list(s.aph)
    win = lose = False
    W, L, w, h = st.walls, st.lava, st.w, st.h
    n_aspd0, n_aph0 = len(aspd), len(aph)
    has_ph = bool(aph)

    def lava_chk():
        nonlocal hp, lose, ashd
        if pos not in L:
            return
        if has_ph or len(aph) > 0:
            return
        if ashd:
            mi = min(range(len(ashd)), key=lambda i: ashd[i])
            ashd[mi] -= 1
            if ashd[mi] <= 0: ashd.pop(mi)
        else:
            hp -= 2
            if hp <= 0: lose = True

    if act in _DIR:
        dx, dy = _DIR[act]
        nsub = 2 if aspd else 1
        for _ in range(nsub):
            nx, ny = pos[0] + dx, pos[1] + dy
            if not (0 <= nx < w and 0 <= ny < h):
                if pos in L: lava_chk()
                break
            tgt = (nx, ny)
            moved = False
            if tgt in W:
                if has_ph: pos = tgt; moved = True
            elif tgt in doors:
                if has_ph: pos = tgt; moved = True
            elif tgt in boxes:
                bx, by = nx + dx, ny + dy
                ok = (0 <= bx < w and 0 <= by < h
                      and (bx, by) not in W and (bx, by) not in doors
                      and (bx, by) not in boxes and (bx, by) not in L)
                if ok:
                    boxes = (boxes - frozenset({tgt})) | frozenset({(bx, by)})
                    pos = tgt; moved = True
                elif has_ph:
                    pos = tgt; moved = True
            else:
                pos = tgt; moved = True
            if pos in L: lava_chk()
            if lose: break
            if pos == st.exit and not gems: win = True; break
            if not moved: break

    elif act == Action.PICK_UP:
        p = pos
        if p in co:  sc += 5;  co = co - frozenset({p})
        if p in gems: gems = gems - frozenset({p})
        if p in kg:  nk += 1;  kg = kg - frozenset({p})
        if p in spu: aspd.append(5); spu = spu - frozenset({p})
        if p in hpu: ashd.append(5); hpu = hpu - frozenset({p})
        if p in ppu: aph.append(5);  ppu = ppu - frozenset({p})
        if pos in L and not (len(aph) > 0):
            if ashd:
                mi = min(range(len(ashd)), key=lambda i: ashd[i])
                ashd[mi] -= 1
                if ashd[mi] <= 0: ashd.pop(mi)
            else:
                hp -= 2
                if hp <= 0: lose = True
        if pos == st.exit and not gems: win = True

    elif act == Action.USE_KEY:
        if nk > 0:
            for ddx, ddy in _ADJ4:
                adj = (pos[0] + ddx, pos[1] + ddy)
                if adj in doors:
                    nk -= 1; doors = doors - frozenset({adj}); break
        if pos in L: lava_chk()

    else:  # WAIT
        if pos in L: lava_chk()

    if not win and not lose:
        sc -= st.cost

    tspd = [t - 1 for t in aspd[:n_aspd0] if t > 1] + aspd[n_aspd0:]
    taph = [t - 1 for t in aph[:n_aph0] if t > 1] + aph[n_aph0:]
    tashd = [x for x in ashd if x > 0]

    turn = s.turn + 1
    if st.tlim is not None and turn >= st.tlim and not win:
        lose = True

    return _S(pos, hp, nk, sc, turn, gems, doors, boxes, kg, co,
              spu, hpu, ppu,
              tuple(sorted(tspd)), tuple(sorted(tashd)), tuple(sorted(taph)),
              win, lose)


def _heuristic(s, st):
    if s.win: return 0
    pos, ex, cost = s.pos, st.exit, st.cost
    gems = s.gems
    spd = max(s.aspd, default=0)

    def _sd(D):
        if spd <= 0 or D <= 0: return D
        return D - spd if D > 2 * spd else (D + 1) // 2

    if not gems:
        return cost * _sd(abs(pos[0]-ex[0]) + abs(pos[1]-ex[1]))
    gl = list(gems); n = len(gl)
    da = [abs(pos[0]-g[0]) + abs(pos[1]-g[1]) for g in gl]
    de = [abs(g[0]-ex[0]) + abs(g[1]-ex[1]) for g in gl]
    if n == 1:
        return cost * _sd(da[0] + 1 + de[0])
    dg = [[abs(gl[i][0]-gl[j][0]) + abs(gl[i][1]-gl[j][1])
           for j in range(n)] for i in range(n)]
    INF = float("inf"); full = (1 << n) - 1
    dp = [[INF]*n for _ in range(1 << n)]
    for i in range(n): dp[1 << i][i] = da[i]
    for mask in range(1, 1 << n):
        for last in range(n):
            if not (mask & (1 << last)) or dp[mask][last] == INF: continue
            for nx in range(n):
                if mask & (1 << nx): continue
                nm = mask | (1 << nx)
                v = dp[mask][last] + dg[last][nx]
                if v < dp[nm][nx]: dp[nm][nx] = v
    best = min((dp[full][i] + de[i] for i in range(n)), default=INF)
    if best == INF: return 0
    return cost * _sd(best + n)


def _actions(s, st):
    out = []; pos = s.pos; ph = bool(s.aph)
    for a in _MOVES:
        dx, dy = _DIR[a]; nx, ny = pos[0]+dx, pos[1]+dy
        if not (0 <= nx < st.w and 0 <= ny < st.h): continue
        tgt = (nx, ny)
        if tgt in st.walls:
            if not ph: continue
        elif tgt in s.doors:
            if not ph: continue
        elif tgt in s.boxes and not ph:
            bx, by = nx+dx, ny+dy
            if not (0 <= bx < st.w and 0 <= by < st.h): continue
            if (bx,by) in st.walls or (bx,by) in s.doors or (bx,by) in s.boxes or (bx,by) in st.lava:
                continue
        out.append(a)
    if pos in s.co or pos in s.gems or pos in s.kg or pos in s.spu or pos in s.hpu or pos in s.ppu:
        out.append(Action.PICK_UP)
    if s.nk > 0:
        for ddx, ddy in _ADJ4:
            if (pos[0]+ddx, pos[1]+ddy) in s.doors:
                out.append(Action.USE_KEY); break
    return out


_MAX_POPS = 2_000_000
_COIN_THRESH = 20


def _astar(init, st, budget):
    t0 = time.time()
    ik = _skey(init)
    ig = init.turn * st.cost
    ih = _heuristic(init, st)
    cnt = 0
    heap = [(ig + ih, cnt, ig, init)]; cnt += 1
    best = {ik: ig}
    parent = {}
    pops = 0
    while heap:
        pops += 1
        if pops & 0x3FF == 0:
            if pops >= _MAX_POPS or time.time() - t0 > budget:
                break
        f, _, g, s = heapq.heappop(heap)
        sk = _skey(s)
        if g > best.get(sk, float("inf")): continue
        if s.win:
            path = []; k = sk
            while k != ik:
                pk, a = parent[k]; path.append(a); k = pk
            path.reverse(); return path
        for a in _actions(s, st):
            ns = _sim(s, a, st)
            if ns.lose: continue
            nk = _skey(ns); ng = ns.turn * st.cost
            if ng >= best.get(nk, float("inf")): continue
            best[nk] = ng
            parent[nk] = (sk, a)
            heapq.heappush(heap, (ng + _heuristic(ns, st), cnt, ng, ns))
            cnt += 1
    return []


def _astar_score(init, st, budget):
    t0 = time.time()
    ik = _skey_co(init)
    ig = -init.sc
    ih = _heuristic(init, st)
    cnt = 0
    heap = [(ig + ih, cnt, ig, init)]; cnt += 1
    best = {ik: ig}
    parent = {}
    pops = 0
    best_win_g = float("inf")
    best_win_sk = None
    while heap:
        pops += 1
        if pops & 0x3FF == 0:
            if pops >= 500_000 or time.time() - t0 > budget:
                break
        f, _, g, s = heapq.heappop(heap)
        sk = _skey_co(s)
        if g > best.get(sk, float("inf")): continue
        if s.win:
            if g < best_win_g:
                best_win_g = g; best_win_sk = sk
            continue
        for a in _actions(s, st):
            ns = _sim(s, a, st)
            if ns.lose: continue
            nsk = _skey_co(ns); ng = -ns.sc
            if ng >= best.get(nsk, float("inf")): continue
            if ng >= best_win_g: continue
            best[nsk] = ng
            parent[nsk] = (sk, a)
            heapq.heappush(heap, (ng + _heuristic(ns, st), cnt, ng, ns))
            cnt += 1
    if best_win_sk is None: return []
    path = []; k = best_win_sk
    while k != ik:
        pk, a = parent[k]; path.append(a); k = pk
    path.reverse(); return path


def _collect_coins(path, init, st):
    if not path:
        return path
    slack = (st.tlim - init.turn - len(path)) if st.tlim else 999
    if slack <= 0:
        return path
    result = []
    s = init
    extra = 0
    for a in path:
        if (extra < slack and s.pos in s.co and not s.win and not s.lose
                and a != Action.PICK_UP):
            result.append(Action.PICK_UP)
            s = _sim(s, Action.PICK_UP, st)
            extra += 1
            if s.win or s.lose:
                return result
        result.append(a)
        s = _sim(s, a, st)
        if s.win or s.lose:
            return result
    if extra < slack and s.pos in s.co and not s.win and not s.lose:
        result.append(Action.PICK_UP)
    return result


def _path_score(path, init, st):
    s = init
    for a in path:
        s = _sim(s, a, st)
        if s.lose: return float('-inf')
        if s.win: return s.sc
    return s.sc if s.win else float('-inf')


# ── Agent ─────────────────────────────────────────────────────

class Agent:
    def __init__(self):
        self._plan = []
        self._idx = 0
        self._fail = False

    def step(self, state: GridState | ImageObservation) -> Action:
        if self._fail:
            return Action.WAIT
        if self._idx < len(self._plan):
            a = self._plan[self._idx]; self._idx += 1; return a
        if not isinstance(state, GridState):
            state = self.parse(state)
        if self._fail:
            return Action.WAIT

        st, s0 = _extract(state)
        t0 = time.time()
        n_coins = len(s0.co)
        total_budget = 13.0 if st.w * st.h >= 144 else 4.0

        b1 = min(2.0, total_budget * 0.3) if 0 < n_coins <= _COIN_THRESH else total_budget
        path = _astar(s0, st, b1)
        if not path:
            self._fail = True; return Action.WAIT
        raw_sc = _path_score(path, s0, st)
        path_c = _collect_coins(path, s0, st)
        if _path_score(path_c, s0, st) > raw_sc:
            path = path_c

        elapsed = time.time() - t0
        remaining = total_budget - elapsed
        if remaining > 0.3 and 0 < n_coins <= _COIN_THRESH:
            path2 = _astar_score(s0, st, remaining - 0.1)
            if path2:
                raw2 = _path_score(path2, s0, st)
                path2c = _collect_coins(path2, s0, st)
                if _path_score(path2c, s0, st) > raw2:
                    path2 = path2c
                if _path_score(path2, s0, st) > _path_score(path, s0, st):
                    path = path2

        self._plan = path
        self._idx = 1
        return self._plan[0]

    # ── Image parsing (Task 2 / 3) ───────────────────────────

    def parse(self, observation: ImageObservation) -> GridState:
        info = observation["info"]; cfg = info["config"]; sts = info["status"]
        gs = GridState(
            width=cfg["width"], height=cfg["height"],
            movement=MOVEMENTS["cardinal"],
            objective=OBJECTIVES["collect_gems_and_exit"],
            step_cost=STEP_COST,
            seed=None if cfg["seed"] == -1 else cfg["seed"],
            turn=sts["turn"], score=sts["score"],
            win=sts["phase"] == "win", lose=sts["phase"] == "lose",
            message=info["message"] or None,
            turn_limit=None if cfg["turn_limit"] == -1 else cfg["turn_limit"],
        )
        img = observation["image"]
        ih, iw = img.shape[:2]
        W, H = cfg["width"], cfg["height"]
        model = _get_ml_model()
        agent_ent = None
        for y in range(H):
            for x in range(W):
                y0 = y * ih // H; y1 = (y + 1) * ih // H
                x0 = x * iw // W; x1 = (x + 1) * iw // W
                cell = img[y0:y1, x0:x1]
                cell_img = Image.fromarray(cell).resize((_CELL_SIZE, _CELL_SIZE))
                arr = np.asarray(cell_img)[:, :, :3].flatten().astype(np.float32) / 255.0
                label = model.predict(arr.reshape(1, -1))[0]
                etype = _LABEL_TO_TYPE[label]
                if etype is None or etype is UnlockedDoorEntity:
                    continue
                ent = etype()
                if isinstance(ent, AgentEntity):
                    ent.set_health(info["agent"]["health"]["current_health"])
                    for item in info["agent"]["inventory"]:
                        if item["type"] == "key":
                            ent.inventory_list.append(KeyEntity())
                    for eff in info["agent"]["effects"]:
                        if eff["type"] == "SPEED" and eff["limit_amount"] > 0:
                            e = SpeedPowerUpEntity()
                            e.time_limit = TimeLimit(amount=eff["limit_amount"])
                            ent.status_list.append(e)
                        elif eff["type"] == "IMMUNITY" and eff["limit_amount"] > 0:
                            e = ShieldPowerUpEntity()
                            e.usage_limit = UsageLimit(amount=eff["limit_amount"])
                            ent.status_list.append(e)
                        elif eff["type"] == "PHASING" and eff["limit_amount"] > 0:
                            e = PhasingPowerUpEntity()
                            e.time_limit = TimeLimit(amount=eff["limit_amount"])
                            ent.status_list.append(e)
                    agent_ent = ent
                gs.add((x, y), ent)
        return gs

    def info(self) -> dict[str, str]:
        return {"name": "A* Agent"}
