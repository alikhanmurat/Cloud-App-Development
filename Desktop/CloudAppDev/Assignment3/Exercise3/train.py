import pandas as pd
import tensorflow as tf

def load_data():
    df = pd.read_csv('gs://cad-assignment3-1/data.csv')
    X_train = df[['feature1', 'feature2']].values  
    y_train = df['label'].values  
    return X_train, y_train

def create_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(10, activation='relu', input_shape=(2,)),  
        tf.keras.layers.Dense(1, activation='sigmoid')  
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy']) 
    return model

def main():
    X_train, y_train = load_data()
    
    model = create_model()
    train_data = tf.data.Dataset.from_tensor_slices((X_train, y_train)).batch(32)
    model.fit(train_data, epochs=5)
    
    model.save('gs://cad-assignment3-1/model') 

if __name__ == '__main__':
    main()
