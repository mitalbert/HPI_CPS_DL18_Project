import json
import ntpath

#return from the input file only dict of id & name
def conv_input(input_data):
    id_img = dict()
    for entry in input_data['images']:
        id_img[entry['id']] = entry['file_name']
    return id_img


def search(name, output):
    return [element for element in output if getFilename(element['image_name']) == name]

#Get file name from the image_fn which include path
def getFilename(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

#Adjust the output of Captionme with the submission output format
def covert_output (input_dic , output_dict):
    data3=[]
    for key , value in input_dic.items():
        name = value
        e = search(name, output_dict)
        if (len(e) > 0):
            data3.append({'image_id' : key , 'caption' : e[0]['caption']})
    with open('results.json', 'w') as file:
         file.write(json.dumps(data3))


#assert os.path.isfile("/home/mital/docker/sample-submission/input.json"), "Input JSON missing!"

with open ('output.json') as f1:
    captionme_dict = json.load(f1)
with open ('input2.json') as f2:
    input_data = json.load(f2)

adj_input= conv_input(input_data)
covert_output(adj_input, captionme_dict)

