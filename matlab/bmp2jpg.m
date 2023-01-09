clear 

for i=0:9
    InImgName=sprintf('GRAY000%d.bmp',i);%错eval('GRAY0000',i,'.bmp');
    I=imread(InImgName);
    OutImgName=sprintf('GRAY000%d.jpg',i);%
    imwrite(I,OutImgName)
end

for i=10:99
    InImgName=sprintf('GRAY00%d.bmp',i);%错eval('GRAY0000',i,'.bmp');
    I=imread(InImgName);
    OutImgName=sprintf('GRAY00%d.jpg',i);%
    imwrite(I,OutImgName)
end

for i=100:299
    InImgName=sprintf('GRAY0%d.bmp',i);%错eval('GRAY0000',i,'.bmp');
    I=imread(InImgName);
    OutImgName=sprintf('GRAY0%d.jpg',i);%
    imwrite(I,OutImgName)
end