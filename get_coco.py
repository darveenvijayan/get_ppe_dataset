

# I downloaded the images with the code below. Now I think that I need the annotations (bounding boxes and labels).


from pycocotools.coco import COCO
import requests

coco = COCO('instances_train2017.json')
cats = coco.loadCats(coco.getCatIds())
nms=[cat['name'] for cat in cats]
print('COCO categories: \n{}\n'.format(' '.join(nms)))



catIds = coco.getCatIds(catNms=['cell phone'])
imgIds = coco.getImgIds(catIds=catIds )
images = coco.loadImgs(imgIds)
print("imgIds: ", imgIds)
print("images: ", images)

for im in images:
    print("im: ", im)
    img_data = requests.get(im['coco_url']).content

    with open('/downloaded_images/' + im['file_name'], 'wb') as handler:
        handler.write(img_data)




# Annotations seem to be downloaded this way:


#Download annotations
with open('/downloaded_images/annotations_download_' + classes + '.txt', mode='w', newline='') as annot:

        for im in images:
                annIds = coco.getAnnIds(imgIds=im['id'], catIds=catIds, iscrowd=None)
                anns = coco.loadAnns(annIds)

        for i in range(len(anns)):
                annot_writer = csv.writer(annot)

                annot_writer.writerow(['/downloaded_images/' + im['file_name'],
                        0,
                        round(int(round(anns[i]['bbox'][0]))/im['width'],5), 
                        round(int(round(anns[i]['bbox'][1]))/im['height'],5), 
                        round(int(round(anns[i]['bbox'][3]))/im['width'],5), 
                        round(int(round(anns[i]['bbox'][1]))/im['height'],5)])

                print('/downloaded_images/' + im['file_name'],
                        0,
                        round(int(round(anns[i]['bbox'][0]))/im['width'],5), 
                        round(int(round(anns[i]['bbox'][1]))/im['height'],5), 
                        round(int(round(anns[i]['bbox'][3]))/im['width'],5), 
                        round(int(round(anns[i]['bbox'][1]))/im['height'],5))
                annot.close()

