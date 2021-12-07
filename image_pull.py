def convert(txt_file, n_images):
  lbl_f = open("data/MNIST/raw/t10k-labels-idx1-ubyte", "rb")   # MNIST has labels (digits)
  img_f = open("data/MNIST/raw/t10k-images-idx3-ubyte", "rb")     # and pixel vals separate
  txt_f = open(txt_file, "w")      # output file to write to

  img_f.read(16)   # discard header info
  lbl_f.read(8)    # discard header info
  txt_f.write("{\n")  # next image
  for i in range(n_images):   # number images requested
    txt_f.write(f"\t\"image{i}\" : [\n")  # next image
    lbl = ord(lbl_f.read(1))  # get label (unicode, one byte)
    for j in range(783):  # get 784 vals from the image file
      val = ord(img_f.read(1))
      txt_f.write("\t\t" + str(val) + ","+"\n")
    val = ord(img_f.read(1))
    txt_f.write("\t\t" + str(val) + "\n")  # will leave a trailing space
    txt_f.write("\t],\n")  # next image
  txt_f.write("}\n")  # next image

  img_f.close(); txt_f.close(); lbl_f.close()

def main():
  convert("mnist_test.json", 10)

if __name__ == "__main__":
  main()
