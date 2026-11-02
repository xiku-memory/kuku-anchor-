# -*- coding: utf-8 -*-
"""建骨架：不覆盖已有文件；例子全是空的，因为它们该由你填。"""
import io, os, shutil, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
TPL = os.path.join(HERE, "templates")
DIRS = ["记忆核心", "原文", "工具", "对外"]
MAKE = {
    "原文/说明.md": "# 原文\n\n> 这里放**逐字记录**，带时间戳。\n> 全库唯一一份原料；别的地方只留理解、只留指针。\n",
    "对外/说明.md": "# 对外\n\n> 这里只放你对人的**理解**，不放原话；原话指回 原文/。\n> 空着就空着——空着不是没有，是还没发现。\n",
}

def main():
    for d in DIRS:
        os.makedirs(d, exist_ok=True)
    copied, skipped = [], []
    for name in sorted(os.listdir(TPL)):
        src = os.path.join(TPL, name)
        dst = os.path.join("记忆核心", name)
        if os.path.exists(dst):
            skipped.append(name); continue
        shutil.copy(src, dst); copied.append(name)
    for rel, body in MAKE.items():
        if os.path.exists(rel):
            skipped.append(rel); continue
        os.makedirs(os.path.dirname(rel), exist_ok=True)
        io.open(rel, "w", encoding="utf-8").write(body)
        copied.append(rel)
    print("建好 %d 个，跳过 %d 个（你已经有它了）" % (len(copied), len(skipped)))
    for c in copied: print("  +", c)
    for s in skipped: print("  = 跳过", s)
    print()
    print("模板里的例子都是空的，因为它们该由你填。")
    print("填不出来不是错，空着的格子就是「还没发现」。")

if __name__ == "__main__":
    main()
