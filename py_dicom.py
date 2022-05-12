import pydicom as dicom
import matplotlib.pylab as plt
import os
import cv2
import multiprocessing
from datetime import datetime

time_list = {}
FMT = '%H:%M:%S'

dirs = 'HCMtest/'


def process1(procnum):
    start = datetime.now().strftime(FMT)

    file_dir = os.listdir(dirs)
    for path in file_dir:
        if 'dcm' in path:
            image_path = dirs+path
            ds = dicom.dcmread(image_path)
            pixel_array_numpy = ds.pixel_array
            image_format = '.png'  # or '.png'
            image_path = image_path.replace('.dcm', image_format)
            res = cv2.imwrite(image_path, pixel_array_numpy)
            if res == False:
                for i, slice in enumerate(pixel_array_numpy):
                    image_format = '.png'  # or '.png'
                    image_path = image_path.replace('.dcm', image_format)
                    res = cv2.imwrite(image_path, slice)
                    break

    stop = datetime.now().strftime(FMT)
    time_taken1 = datetime.strptime(
        str(stop), FMT) - datetime.strptime(str(start), FMT)
    print(time_taken1, '-----------------------P1---------------------------')
    return time_taken1


def process2(procnum):
    start = datetime.now().strftime(FMT)

    file_dir = os.listdir(dirs)
    for path in file_dir:
        if 'dcm' in path:
            image_path = dirs+path
            # ds = dicom.dcmread(dirs+path)
            # print(ds)
            ds = dicom.dcmread(image_path)
            pixel_array_numpy = ds.pixel_array
            image_format = '.png'  # or '.png'
            image_path = image_path.replace('.dcm', image_format)
            # print(image_path, '------------------------')
            res = cv2.imwrite(image_path, pixel_array_numpy)
            if res == False:
                for i, slice in enumerate(pixel_array_numpy):
                    image_format = '.png'  # or '.png'
                    image_path = image_path.replace('.dcm', image_format)
                    res = cv2.imwrite(image_path, slice)
                    break

    stop = datetime.now().strftime(FMT)
    time_taken2 = datetime.strptime(
        str(stop), FMT) - datetime.strptime(str(start), FMT)
    print(time_taken2, '----------------------P2----------------------------')
    return time_taken2


def process3(procnum):
    start = datetime.now().strftime(FMT)

    file_dir = os.listdir(dirs)
    for path in file_dir:
        if 'dcm' in path:
            image_path = dirs+path
            ds = dicom.dcmread(image_path)
            pixel_array_numpy = ds.pixel_array
            image_format = '.png'  # or '.png'
            image_path = image_path.replace('.dcm', image_format)
            res = cv2.imwrite(image_path, pixel_array_numpy)
            if res == False:
                for i, slice in enumerate(pixel_array_numpy):
                    image_format = '.png'  # or '.png'
                    image_path = image_path.replace('.dcm', image_format)
                    res = cv2.imwrite(image_path, slice)
                    break

    stop = datetime.now().strftime(FMT)
    time_taken3 = datetime.strptime(
        str(stop), FMT) - datetime.strptime(str(start), FMT)
    print(time_taken3, '-----------------------P3---------------------------')
    return time_taken3


def process4(procnum):
    start = datetime.now().strftime(FMT)

    file_dir = os.listdir(dirs)
    for path in file_dir:
        if 'dcm' in path:
            image_path = dirs+path
            ds = dicom.dcmread(image_path)
            pixel_array_numpy = ds.pixel_array
            image_format = '.png'  # or '.png'
            image_path = image_path.replace('.dcm', image_format)
            res = cv2.imwrite(image_path, pixel_array_numpy)
            if res == False:
                for i, slice in enumerate(pixel_array_numpy):
                    image_format = '.png'  # or '.png'
                    image_path = image_path.replace('.dcm', image_format)
                    res = cv2.imwrite(image_path, slice)
                    break

    stop = datetime.now().strftime(FMT)
    time_taken4 = datetime.strptime(
        str(stop), FMT) - datetime.strptime(str(start), FMT)
    print(time_taken4, '-----------------------P4---------------------------')
    return time_taken4


if __name__ == '__main__':
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    pool = multiprocessing.Pool(processes=1)
    time_list['process1'] = pool.map(process1, range(1))
    time_list['process2'] = pool.map(process2, range(1))
    time_list['process3'] = pool.map(process3, range(1))
    time_list['process4'] = pool.map(process4, range(1))

print(time_list)
courses = list(time_list.keys())
values = []
for val in list(time_list.values()):
    values.append(val[0].seconds)
print(values, "______VALUES______")
fig = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(courses, values, color='maroon',
        width=0.1)

plt.xlabel("Time Consumed")
plt.ylabel("Time Taken")
plt.title("Time Comparision graph")
plt.ylim(ymin=0)
plt.show()
plt.savefig("performance.png")
