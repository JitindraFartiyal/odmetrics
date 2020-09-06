import numpy

def iou(bboxA, bboxB):
    '''
        Input :
            bboxA : [left, top, right, bottom]
            bboxB : [left, top, right, bottom]   

        Output:
            Intersection over union(iou) between bboxA and bboxB
            Range of iou [0-1]
    '''

    xA = max(bboxA[0], bboxB[0])
    yA = max(bboxA[1], bboxB[1])
    
    xB = min(bboxA[2], bboxB[2])
    yB = min(bboxA[3], bboxB[3])

    intersected_area = (xB - xA)  * (yB - yA)
    
    bboxA_area = (bboxA[2] - bboxA[0]) * (bboxA[3] - bboxA[1])
    bboxB_area = (bboxB[2] - bboxB[0]) * (bboxB[3] - bboxB[1])

    if (bboxA_area + bboxB_area - intersected_area) > 0:
        intersection_over_union = intersected_area / (bboxA_area + bboxB_area - intersected_area)
    else:
        intersection_over_union = 0

    return round(intersection_over_union, 3)
    
if __name__ == '__main__':
    bboxA = [10, 20, 30, 40]
    bboxB = [100, 200, 300, 541]

    print('IOU : ', iou(bboxA, bboxB))