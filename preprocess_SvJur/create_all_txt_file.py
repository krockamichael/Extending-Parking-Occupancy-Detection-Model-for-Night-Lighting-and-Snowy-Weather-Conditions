import os


root_dir = '/mnt/c/Users/krock/Desktop/SvJur'

def update_status(status, space_list, filename, space_position) -> int:
    if status == 1:
        return status
    if any(name in filename for name in space_list):
        if filename.endswith(space_position):
            return 1
    return 0

dir = '2022_02_08'
with open(os.path.join(root_dir, dir, 'all.txt'), 'w') as f:
    for filename in os.listdir(os.path.join(root_dir, dir, 'segmented')):
        entry_name = os.path.join(dir, 'segmented', filename)
        status = 0
        if any(name in filename for name in ['005', '006', '007', '009']):
            if filename.endswith('_13.jpg'):
                status = 1
        f.write(' '.join([entry_name, str(status), '\n']))

dir = '2022_03_07'
with open(os.path.join(root_dir, dir, 'all.txt'), 'w') as f:
    for filename in os.listdir(os.path.join(root_dir, dir, 'segmented')):
        entry_name = os.path.join(dir, 'segmented', filename)
        status = 0
        space_1_list = [str(i).zfill(4) for i in range(89)]
        space_3_list = [str(i).zfill(4) for i in range(8,30)]
        space_4_list = [str(i).zfill(4) for i in range(280,362)]
        status = update_status(status, space_1_list, filename, '_1.jpg')
        status = update_status(status, space_3_list, filename, '_3.jpg')
        status = update_status(status, space_4_list, filename, '_4.jpg')
        f.write(' '.join([entry_name, str(status), '\n']))

dir = '2022_03_14'
with open(os.path.join(root_dir, dir, 'all.txt'), 'w') as f:
    for filename in os.listdir(os.path.join(root_dir, dir, 'segmented')):
        entry_name = os.path.join(dir, 'segmented', filename)
        status = 0
        f.write(' '.join([entry_name, str(status), '\n']))

dir = '2022_03_24'
with open(os.path.join(root_dir, dir, 'all.txt'), 'w') as f:
    for filename in os.listdir(os.path.join(root_dir, dir, 'segmented')):
        entry_name = os.path.join(dir, 'segmented', filename)
        status = 0
        space_2_list = [str(i).zfill(4) for i in range(465)]
        space_3_list = [str(i).zfill(4) for i in range(465)]
        space_5_list = [str(i).zfill(4) for i in range(8)]
        space_1_list = [str(i).zfill(4) for i in range(10,48)]
        status = update_status(status, space_2_list, filename, '_2.jpg')
        status = update_status(status, space_3_list, filename, '_3.jpg')
        status = update_status(status, space_5_list, filename, '_5.jpg')
        status = update_status(status, space_1_list, filename, '_1.jpg')
        f.write(' '.join([entry_name, str(status), '\n']))

dir = '2022_03_26'
with open(os.path.join(root_dir, dir, 'all.txt'), 'w') as f:
    for filename in os.listdir(os.path.join(root_dir, dir, 'segmented')):
        entry_name = os.path.join(dir, 'segmented', filename)
        status = 0
        space_1_list = [str(i).zfill(4) for i in range(26)]
        space_7_list = [str(i).zfill(4) for i in range(761)]
        space_8_list = [str(i).zfill(4) for i in range(26,59)]
        space_9_list = [str(i).zfill(4) for i in range(761)]
        status = update_status(status, space_1_list, filename, '_1.jpg')
        status = update_status(status, space_7_list, filename, '_7.jpg')
        status = update_status(status, space_8_list, filename, '_8.jpg')
        status = update_status(status, space_9_list, filename, '_9.jpg')
        f.write(' '.join([entry_name, str(status), '\n']))

dir = '2022_03_27'
with open(os.path.join(root_dir, dir, 'all.txt'), 'w') as f:
    for filename in os.listdir(os.path.join(root_dir, dir, 'segmented')):
        entry_name = os.path.join(dir, 'segmented', filename)
        status = 0
        space_2_list = [str(i).zfill(4) for i in range(21)]
        space_8_list = [str(i).zfill(4) for i in range(21,32)]
        space_8_list_2 = [str(i).zfill(4) for i in range(139,767)]
        space_10_list = [str(i).zfill(4) for i in range(767)]
        status = update_status(status, space_2_list, filename, '_2.jpg')
        status = update_status(status, space_8_list, filename, '_8.jpg')
        status = update_status(status, space_8_list_2, filename, '_8.jpg')
        status = update_status(status, space_10_list, filename, '_10.jpg')
        f.write(' '.join([entry_name, str(status), '\n']))

dir = '2022_03_29'
with open(os.path.join(root_dir, dir, 'all.txt'), 'w') as f:
    for filename in os.listdir(os.path.join(root_dir, dir, 'segmented')):
        entry_name = os.path.join(dir, 'segmented', filename)
        status = 0
        space_1_list = [str(i).zfill(4) for i in range(22,32)]
        space_1_list_2 = [str(i).zfill(4) for i in range(68,134)]
        space_2_list = [str(i).zfill(4) for i in range(753)]
        space_3_list = [str(i).zfill(4) for i in range(753)]
        space_4_list = [str(i).zfill(4) for i in range(0,19)]
        status = update_status(status, space_1_list, filename, '_1.jpg')
        status = update_status(status, space_1_list_2, filename, '_1.jpg')
        status = update_status(status, space_2_list, filename, '_2.jpg')
        status = update_status(status, space_3_list, filename, '_3.jpg')
        status = update_status(status, space_4_list, filename, '_4.jpg')
        f.write(' '.join([entry_name, str(status), '\n']))
