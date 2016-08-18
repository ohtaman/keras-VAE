from keras.datasets import mnist
from vae_m1 import VAEM1

nb_epoch = 1


if __name__ == '__main__':
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    X_train = X_train.reshape(-1, 28*28)
    X_test = X_test.reshape(-1, 28*28)


    vaem1 = VAEM1()

    training = vaem1.training_model()
    training.compile(optimizer='rmsprop', loss=vaem1.cost)
    training.fit(X_train, X_train,
                 batch_size=100,
                 nb_epoch=nb_epoch,
                 shuffle=True,
                 validation_data=(X_test, X_test)
                 )

    encoder = vaem1.encoder()
    encoder.save('./trained_model/encoder_m1.h5')
    decoder = vaem1.decoder()
    decoder.save('./trained_model/decoder_m1.h5')



