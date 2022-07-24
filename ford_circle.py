import math
import tkinter as tk


def calcFarey(N):
    res = [[[0, 1], [1, 1]]]
    for idx in range(N - 1):
        tmp = []
        for f in range(len(res[idx]) - 1):
            bunshi = res[idx][f][0] + res[idx][f + 1][0]
            bunbo = res[idx][f][1] + res[idx][f + 1][1]
            GCD_Num = math.gcd(bunshi, bunbo)
            bunshi = bunshi // GCD_Num
            bunbo = bunbo // GCD_Num
            tmp.append(res[idx][f])
            if bunbo > idx + 2:
                continue
            tmp.append([bunshi, bunbo])
        tmp.append([1, 1])
        res.append(tmp)
    return res


def drawFarey(farey, N):
    root = tk.Tk()
    root.title("Ford circle")
    MaxSize = 600
    blank = 8
    root.geometry(str(MaxSize + blank * 2) + "x" + str(MaxSize + blank * 2))
    canvas = tk.Canvas(root, bg="white")
    canvas.pack(fill=tk.BOTH, expand=True)
    for f in farey:
        cx = MaxSize * (f[0] / f[1])
        cy = MaxSize * (1 / (f[1] * f[1] * 2))
        r = MaxSize * (1 / (f[1] * f[1] * 2))
        canvas.create_oval(
            blank + cx - r,
            blank + MaxSize - cy - r,
            blank + cx + r,
            blank + MaxSize - cy + r,
            width=2,
            fill="white",
        )
    canvas.create_line(
        0, blank + MaxSize, MaxSize + blank * 2, blank + MaxSize, width=2
    )
    root.mainloop()


N = int(input())
Farey = calcFarey(N)
drawFarey(Farey[-1], N)
