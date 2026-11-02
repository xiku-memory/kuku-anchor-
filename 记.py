# -*- coding: utf-8 -*-
"""写一条记录：时间由系统取，不许手打。"""
import datetime, io, os, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

def main(argv):
    if not argv:
        print('用法: python 记.py "你想记的那一下"'); return 1
    text = " ".join(argv).strip()
    now = datetime.datetime.now()
    path = os.path.join("记忆核心", "值得记.md")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path):
        io.open(path, "w", encoding="utf-8").write("# 值得记\n\n")
    blk = "\n## %s\n\n%s\n" % (now.strftime("%Y-%m-%d %H:%M"), text)
    with io.open(path, "a", encoding="utf-8") as f:
        f.write(blk)
    print("已写入", path, "（时间由系统取：%s）" % now.strftime("%H:%M"))
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
