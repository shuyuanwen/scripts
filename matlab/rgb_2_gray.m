for i=0:9
    InImgName=sprintf('./left/img%d.bmp',i);%错eval('GRAY0000',i,'.bmp');
    RGB=imread(InImgName);
    Gray=rgb2gray(RGB);
    OutImgName=sprintf('./gray_left/img%d.bmp',i);%
    imwrite(Gray,OutImgName)
end

for i=0:9
    InImgName=sprintf('./right/img%d.bmp',i);%错eval('GRAY0000',i,'.bmp');
    RGB=imread(InImgName);
    Gray=rgb2gray(RGB);
    OutImgName=sprintf('./gray_right/img%d.bmp',i);%
    imwrite(Gray,OutImgName)
end

for i=10:27
    InImgName=sprintf('./left/img%d.bmp',i);%错eval('GRAY0000',i,'.bmp');
    RGB=imread(InImgName);
    Gray=rgb2gray(RGB);
    OutImgName=sprintf('./gray_left/img%d.bmp',i);%
    imwrite(Gray,OutImgName)
end

for i=10:27
    InImgName=sprintf('./right/img%d.bmp',i);%错eval('GRAY0000',i,'.bmp');
    RGB=imread(InImgName);
    Gray=rgb2gray(RGB);
    OutImgName=sprintf('./gray_right/img%d.bmp',i);%
    imwrite(Gray,OutImgName)
end