#coding=utf-8
import cv2
import os

# 使用mask和原图进行与操作
# 使用时需要将mask和原图放在两个路径下，顺序相同
# mask为png
# 原图为jpg
# 结果为jpg

def combine(srcdir,mskdir,dstdir):

    srclist = os.listdir(srcdir)
    msklist = os.listdir(mskdir)

    if(len(srclist)!=len(msklist)):
        raise EnvironmentError("Numbers do not equal.")
    num = len(srclist)

    for i in range(num):
        img = cv2.imread(srcdir + srclist[i])
        img = cv2.resize(img,(224,224))

        msk = cv2.imread(mskdir + msklist[i],0)

        result = cv2.bitwise_and(img, img, mask=msk)

        savepath = dstdir+srclist[i]

        cv2.imwrite(savepath,result,[int( cv2.IMWRITE_JPEG_QUALITY), 100])
        print(srclist[i]+ ' is successfully saved to path:' + savepath)

        # cv2.imshow("ori",img)
        # cv2.waitKey(0)
        #
        # cv2.imshow("msk",msk)
        # cv2.waitKey(0)
        #
        # cv2.imshow("rst",result)
        # cv2.waitKey(0)



def main():
    originaldir = '/Users/shenyi/Desktop/ori/'
    maskdir = '/Users/shenyi/Desktop/msk/'
    destinationdir = '/Users/shenyi/Desktop/dst/'

    combine(originaldir,maskdir,destinationdir)

if __name__ == '__main__':
    main()

