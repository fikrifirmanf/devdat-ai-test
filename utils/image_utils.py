import tensorflow as tf

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

def validate_image(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_image(image_path):
    img = tf.keras.utils.load_img(
        image_path, target_size=(150, 150)
    )

    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch
    
    return img_array