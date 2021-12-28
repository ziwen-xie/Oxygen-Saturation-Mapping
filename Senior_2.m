%%
global...
    frameNumber...
    video...
    hueThreshold...
    roiPosition...
    imageAxes;

%Name of the video file
filename={'IMG_5745.MOV'}; 

%Read the video as a video object
video=VideoReader(filename{1});

%Initial video frame nember to extract from the video object
frameNumber= min(10, video.NumFrames);

%Fetch the data for the current frame
getFrame();

%Create a new figure
fig=figure(1);
fig.Position=[100,100,video.Width /2, video.Height /2 + 200];

%Default Threshold values for hue
hueThreshold=[0,1];

%Default values for ROI position
roiPosition=[100,100,100,100];

%Create controls for HSV filtering, frame selection, and displaying the
%image as black and white
imagePanel=uipanel(fig,'Position',[0 0 1 0.8]);
imageAxes=axes('Parent', imagePanel);
imageAxes.InnerPosition=[0 0 1 1];

%Show an image of the current image in the figure window
showImage();

function getFrame()
global video frameNumber frame hsvImage;

%Extract the current frame from the video. This returns the frame as a
%multidimentinal array of size w*h*3, where the third dimension represents
%the RGB values for each pixel
frame=read(video,frameNumber);

%Covert the image to hsv color space
hsvImage=rgb2hsv(frame);
end



function roiEvent(src,event)
global roiPosition;
roiPosition = event.CurrentPosition;
display(append(...
    "Position:",...
    num2str(roiPosition)));
end
        
        
function showImage()
global hsvImage hueThreshold frame roiPosition ...
 imageAxes bwImage;

%Copy the frame data to a new variable where we will apply the masking and
%hue thresholding
maskedImage=frame;

%Create a mask based on hue thresholding
hsvMask=hsvImage(:,:,1) >= hueThreshold(1)...
    &hsvImage(:,:,1) <= hueThreshold(2);
%Apply the mask to copied image data, setting pixels that do not meet the
%hue threshold values to zero. If the bwImage option is set to true, also
%set the other pixel to full intensity (255).
maskedImage(repmat(~hsvMask,[1 1 3])) = 0;
if bwImage
    maskedImage(repmat(hsvMask,[1 1 3])) = 255;
end

%Show the image in the figure window, specifically in the figure axes
%(imageAxes) that were created for imagepanel
imshow(maskedImage, 'Parent', imageAxes);

%Draw an interactive circular ROI to isolate the cup. ROT stands for region
%of interest and is a common term in image processing
roi= drawrectangle(...
    'Parent', imageAxes,...
    'Color','r', ...
    'Position',roiPosition);

%Add a listener to the roiso that the function roiEvent is called whenever
%a change is made tothe size or position of the circle
addlistener(roi,'ROIMoved',@roiEvent);
end