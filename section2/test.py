import sys
import io
import urllib.request as dw

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')



imgUrl="https://ssl.pstatic.net/tveta/libs/1273/1273252/9eb8600d254abf1b4a8f_20200131154850603.jpg"
mp4Url="https://tvetamovie.pstatic.net/libs/1260/1260649/24e0cefb7bd741f2d0ec_20200211143216244.mp4-pBASE-v0-f98576-20200211143324330.mp4"

savePath1="D:/atom_py/test2.jpg"
savePath2="D:/atom_py/test3.mp4"

dw.urlretrieve(imgUrl,savePath1)
dw.urlretrieve(mp4Url,savePath2)

print("완료")
