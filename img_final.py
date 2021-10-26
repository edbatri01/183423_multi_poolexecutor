from concurrent.futures import ThreadPoolExecutor
from imgurpython import ImgurClient
from multiprocessing import Pool
import os
import urllib.request
import timeit
import concurrent.futures
 
secreto_cliente = "5f8c3cce299db5e26a2eb96b0b7809a82805c9ad"
id_cliente = "bfa0e227a1c5643"
 
cliente = ImgurClient(id_cliente, secreto_cliente)

link_arr = []
 
 
def descarga_url_img(link):
   print(link)
   nombre_img = link.split("/")[3]
   formato_img = nombre_img.split(".")[1]
   nombre_img = nombre_img.split(".")[0]
   print(nombre_img, formato_img)
   url_local = "/Users/ledub/Pictures/{}.{}"
   urllib.request.urlretrieve(link, url_local.format(nombre_img, formato_img))
 
 
def main():
    id_album = "bUaCfoz"
    imagenes = cliente.get_album_images(id_album)
 
    for i in imagenes:
        link_arr.append(i.link)
        
    

def poolExecutor():
    with concurrent.futures.ThreadPoolExecutor(3) as executor:
        array = []
        for i in link_arr:
            array.append(executor.submit(descarga_url_img, i))
        
        
        

def multiprocessingPool():
    with Pool (len(link_arr)) as p:
        array = []
        for i in link_arr:
            array.append(p.Process(target=descarga_url_img, args=(i,)))

        



 
 
if __name__ == "__main__":
   main()
   print("Tiempo de descarga pool executor {}".format(timeit.Timer(poolExecutor).timeit(number=1)))
   print("Tiempo de descarga multiprocesingPool {}".format(timeit.Timer(poolExecutor).timeit(number=1)))
