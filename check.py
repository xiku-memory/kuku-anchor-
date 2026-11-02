# -*- coding: utf-8 -*-
"""六条校验里能通用的一条：未来时间。红的、灰的分开报。"""
import datetime, glob, io, os, re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PAT = re.compile(r"(20\d{2})-(\d{2})-(\d{2})[ T](\d{2}):(\d{2})")

def main():
    now = datetime.datetime.now()
    today = now.date()
    bad, checked = [], 0
    for path in glob.glob("**/*.md", recursive=True):
        try:
            mtime = datetime.datetime.fromtimestamp(os.path.getmtime(path))
            lines = io.open(path, encoding="utf-8", errors="replace").read().split("\n")
        except Exception as e:
            print("灰：读不了", path, str(e)[:40]); continue
        checked += 1
        for i, line in enumerate(lines, 1):
            for m in PAT.finditer(line):
                try:
                    t = datetime.datetime(*[int(x) for x in m.groups()])
                except ValueError:
                    continue
                if t.date() == mtime.date() and t > mtime + datetime.timedelta(seconds=90):
                    bad.append((path, i, t))
                    break
    print("查了 %d 个 md" % checked)
    if bad:
        for p, i, t in bad[:20]:
            print("  红 %s 第%d行 %s（写在文件修改时间之后）" % (p, i, t.strftime("%m-%d %H:%M")))
        print("共 %d 处。要么写实写时间，要么明写「原定 X，实写 Y」。" % len(bad))
        return 1
    print("未来时间：没有。")
    print("（绿只证明「你写下的这句话今天成立」，不证明别的东西。）")
    return 0

if __name__ == "__main__":
    sys.exit(main())
