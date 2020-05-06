

# I downloaded the images with the code below. Now I think that I need the annotations (bounding boxes and labels).


# from pycocotools.coco import COCO
# import requests
# import csv

# coco = COCO('instances_train2017.json')
# cats = coco.loadCats(coco.getCatIds())
# nms=[cat['name'] for cat in cats]
# print('COCO categories: \n{}\n'.format(' '.join(nms)))



# catIds = coco.getCatIds(catNms=['cell phone'])
# imgIds = coco.getImgIds(catIds=catIds )
# images = coco.loadImgs(imgIds)
# print("imgIds: ", imgIds)
# print("images: ", images)

# for im in images[0:10]:
#         print("im: ", im)
#         img_data = requests.get(im['coco_url']).content

#         with open('/media/darveen/DATADRIVE1/data/yolov3_training_ultralytics/training_prep/downloaded_images/' + im['file_name'], 'wb') as handler:
#                 handler.write(img_data)




# Annotations seem to be downloaded this way:


#Download annotations
# with open('/media/darveen/DATADRIVE1/data/yolov3_training_ultralytics/training_prep/annotations_download_' +  '.txt', mode='w', newline='') as annot:

        # for im in images[0:10]:
        # annIds = coco.getAnnIds(imgIds=im['id'], catIds=catIds, iscrowd=None)
        # anns = coco.loadAnns(annIds)

        # with open('/media/darveen/DATADRIVE1/data/yolov3_training_ultralytics/training_prep/downloaded_images/'+im['file_name'] + '.txt', mode='w', newline='') as annot:
        # annot_writer = csv.writer(annot)
        # for i in range(len(anns)):

        #         annot_writer.writerow(['/media/darveen/DATADRIVE1/data/yolov3_training_ultralytics/training_prep/downloaded_images/' + im['file_name'],
        #                 0,
        #                 round(int(round(anns[i]['bbox'][0]))/im['width'],5), 
        #                 round(int(round(anns[i]['bbox'][1]))/im['height'],5), 
        #                 round(int(round(anns[i]['bbox'][3]))/im['width'],5), 
        #                 round(int(round(anns[i]['bbox'][1]))/im['height'],5)])

        #         print('/media/darveen/DATADRIVE1/data/yolov3_training_ultralytics/training_prep/downloaded_images/' + im['file_name'],
        #                 0,
        #                 round(int(round(anns[i]['bbox'][0]))/im['width'],5), 
        #                 round(int(round(anns[i]['bbox'][1]))/im['height'],5), 
        #                 round(int(round(anns[i]['bbox'][3]))/im['width'],5), 
        #                 round(int(round(anns[i]['bbox'][1]))/im['height'],5))
        #         annot.close()






from pycocotools.coco import COCO
import requests
import csv
import os

working_dir = os.getcwd()

coco = COCO('instances_train2017.json')
cats = coco.loadCats(coco.getCatIds())
nms=[cat['name'] for cat in cats]
# print('COCO categories: \n{}\n'.format(' '.join(nms)))



catIds = coco.getCatIds(catNms=['cell phone'])
imgIds = coco.getImgIds(catIds=catIds )
images = coco.loadImgs(imgIds)
# print("imgIds: ", imgIds)
# print("images: ", images)

for im in images[0:10]:
        # print("im: ", im)
        img_data = requests.get(im['coco_url']).content

        with open('working_dir/downloaded_images/' + im['file_name'], 'wb') as handler:
                handler.write(img_data)

        annIds = coco.getAnnIds(imgIds=im['id'], catIds=catIds, iscrowd=None)
        anns = coco.loadAnns(annIds)

        with open('working_dir/downloaded_images/'+im['file_name'] + '.txt', mode='w', newline='') as annot:
                annot_writer = csv.writer(annot, delimiter=' ')
                for i in range(len(anns)):
                        annot_writer.writerow([
                                0,
                                round(int(round(anns[i]['bbox'][0]))/im['width'],5), 
                                round(int(round(anns[i]['bbox'][1]))/im['height'],5), 
                                round(int(round(anns[i]['bbox'][3]))/im['width'],5), 
                                round(int(round(anns[i]['bbox'][1]))/im['height'],5)])





        # output = []
        # for i in range(len(anns)):

        #         output=[
        #         0,
        #         round(int(round(anns[i]['bbox'][0]))/im['width'],5), 
        #         round(int(round(anns[i]['bbox'][1]))/im['height'],5), 
        #         round(int(round(anns[i]['bbox'][3]))/im['width'],5), 
        #         round(int(round(anns[i]['bbox'][1]))/im['height'],5)
        #         ]


        # print('------------')
        # print(len(anns))



        # with open('/media/darveen/DATADRIVE1/data/yolov3_training_ultralytics/training_prep/downloaded_images/' + im['file_name'],"rt", encoding='ascii') as f:

        #         for row in f:

        #                 output.write(row)
