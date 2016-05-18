from ..feature_extraction.feature_extraction import SparseCoding, Spams, SklearnDL
from ..customutils.customutils import read_dictionary_from_pickle_file, write_dictionary_to_pickle_file
from ..customutils.customutils import read_string_from_file, write_string_to_file
import os, subprocess
import numpy as np
from ..tests.preprocessing_test import test_whitening

from sklearn.utils.validation import NotFittedError

THIS_FILE_PATH = os.path.dirname(os.path.realpath(__file__))


class JoachimsSVM(object):
    
    SVM_LEARN_EXE_PATH = os.path.realpath(os.path.join(THIS_FILE_PATH,
                             "./joachims/svm_multiclass/svm_multiclass_learn"))
    SVM_CLASSIFY_EXE_PATH = os.path.realpath(os.path.join(THIS_FILE_PATH,
                             "./joachims/svm_multiclass/svm_multiclass_classify"))
    
    DEFAULT_MODEL_FILENAME = os.path.realpath(os.path.join(THIS_FILE_PATH,
                             "../tests/data/classification_model_svmlight.pkl"))
    DEFAULT_TRAINED_MODEL_FILENAME = os.path.realpath(os.path.join(THIS_FILE_PATH,
                             "../tests/data/trained_classification_model_svmlight.pkl"))

    TEMP_TRAIN_FILENAME = os.path.realpath(os.path.join(THIS_FILE_PATH,
                                                        "./joachims/temp/sparsex_temp_joachimssvm_train_file"))
    TEMP_TEST_FILENAME = os.path.realpath(os.path.join(THIS_FILE_PATH,
                                                       "./joachims/temp/sparsex_temp_joachimssvm_test_file"))
    TEMP_MODEL_FILENAME = os.path.realpath(os.path.join(THIS_FILE_PATH,
                                                        "./joachims/temp/sparsex_temp_joachimssvm_model_file"))
    TEMP_OUTPUT_FILENAME = os.path.realpath(os.path.join(THIS_FILE_PATH,
                                                        "./joachims/temp/sparsex_temp_joachimssvm_output_file"))
    
    DEFAULT_MODEL_PARAMS = {"model":"", "c":0.1, "t":1, "d":2}
    
    def __init__(self, model_filename=None):
        if model_filename is not None:
            self.load_model(model_filename)
        else:
            self.params = JoachimsSVM.DEFAULT_MODEL_PARAMS


    def save_model(self, filename):
        write_dictionary_to_pickle_file(filename, self.params)


    def load_model(self, filename):
        self.params = read_dictionary_from_pickle_file(filename)


    def train(self, X, Y):
        assert X.ndim == 2, "JoachimsSVM training data X.ndim is %d instead of 2" %X.ndim
        assert Y.ndim == 1, "JoachimsSVM training data Y.ndim is %d instead of 1" %Y.ndim
        
        # convert X and Y into joachims train data format and write to file
        joachims_train_data = self._convert_train_data_to_joachims_train_data(X, Y)
        write_string_to_file(JoachimsSVM.TEMP_TRAIN_FILENAME, joachims_train_data)
        
        #write_string_to_file(JoachimsSVM.TEMP_MODEL_FILENAME, "")
        
        # train the svm model using the train data, model is written to the temp file.
        try:
            args = [JoachimsSVM.SVM_LEARN_EXE_PATH,
                             "-c", str(self.params["c"]),
                             "-t", str(self.params["t"]),
                             "-d", str(self.params["d"]),
                             JoachimsSVM.TEMP_TRAIN_FILENAME,
                             JoachimsSVM.TEMP_MODEL_FILENAME]
            print args
            subprocess.call(args)
            
        except subprocess.CalledProcessError:
            raise subprocess.CalledProcessError("Sparsex Error : Something has gone wrong in training using JoachimsSVM, " \
                                                + "i.e. sparsex/classification/joachims/svm_multiclass/svm_multiclass_learn.")
            
        # load model string from temp model file.
        self.params["model"] = read_string_from_file(JoachimsSVM.TEMP_MODEL_FILENAME)


    def get_predictions(self, X):
        assert X.ndim == 2, "JoachimsSVM prediction data X.ndim is %d instead of 2" %X.ndim
        
        # convert X into joachims test data format and write to file
        joachims_test_data = self._convert_test_data_to_joachims_test_data(X)
        write_string_to_file(JoachimsSVM.TEMP_TEST_FILENAME, joachims_test_data)
        
        # since we are trying to get predictions, we need a valid model file
        if self.params["model"] == "" or self.params["model"] == None:
            raise AttributeError("Sparsex Error : JoachimsSVM model cannot preidct without being trained first. " \
                                 + "Train the classification model at least once to prevent this error.")
        
        # write model string to temp model file
        write_string_to_file(JoachimsSVM.TEMP_MODEL_FILENAME, self.params["model"])
        
        # call the prediction function which writes the predictions to output file
        try:
            subprocess.call([JoachimsSVM.SVM_CLASSIFY_EXE_PATH,
                                     JoachimsSVM.TEMP_TEST_FILENAME,
                                     JoachimsSVM.TEMP_MODEL_FILENAME,
                                     JoachimsSVM.TEMP_OUTPUT_FILENAME])
        except subprocess.CalledProcessError:
            raise subprocess.CalledProcessError("Sparsex Error : Something has gone wrong in predicitions using JoachimsSVM, " \
                                                + "i.e. sparsex/classification/joachims/svm_multiclass/svm_multiclass_classify.")
        
        # read the joachims output from temp output file
        joachims_output = read_string_from_file(JoachimsSVM.TEMP_OUTPUT_FILENAME)
        
        # convert joachims output to predictions format and return them
        return self._convert_joachims_output_to_predictions(joachims_output)
        

    # convert input X,Y into joachims train format of <target> <feature1>:<value1> <feature2>:<value2> ...
    def _convert_train_data_to_joachims_train_data(self, X, Y):
        assert Y.dtype == int, "JoachimsSVM train targets Y.dtype is {0} instead of int/int64".format(Y.dtype)
        print X.shape, X.dtype
        print Y.shape, Y.dtype
        
        
        # target_template = <target>, <integer>
        target_template = "{0}"
        
        # feature_value_template = <feature>:<value>, <integer>:<float>, feature index starts from 1
        feature_value_template = " {0}:{1}"
        
        # each sample will be populated into this string variable
        joachims_train_data = ""
        
        # for every sample
        for sample_index in range(X.shape[0]):
            # add target, e.g. 2
            joachims_train_data += target_template.format(Y[sample_index] + 1)
            
            # add feature:value, e.g. 1:1.33
            for feature_index in range(X.shape[1]):
                joachims_train_data += feature_value_template.format(feature_index + 1, X[sample_index, feature_index])
            
            # finally add newline for each sample
            joachims_train_data += "\n"
        
        return joachims_train_data

    
    # convert input X into joachims test format of <target/placeholder> <feature1>:<value1> <feature2>:<value2> ...
    def _convert_test_data_to_joachims_test_data(self, X):
        raise NotImplementedError
        
    ## convert from svm_light format
    def _convert_joachims_output_to_predictions(self, joachims_output):
        raise NotImplementedError
        
        
        
if __name__ == "__main__":
    image_filename_1 = os.path.realpath(os.path.join(THIS_FILE_PATH, "../tests/data/yaleB01_P00A-005E-10_64x64.pgm"))
    image_filename_2 = os.path.realpath(os.path.join(THIS_FILE_PATH, "../tests/data/yaleB02_P00A-005E-10_64x64.pgm"))
    for message, feature_extraction_library_name, trained_feature_extraction_model_filename, classification_model_filename in zip(
        ["\n### classification using spams feature extraction",
         "\n### classification using spams feature extraction",
         "\n### classification using spams feature extraction",
         "\n### classification using spams feature extraction"],
        [SparseCoding.SKLEARN_DL,
         SparseCoding.SKLEARN_DL,
         SparseCoding.SPAMS,
         SparseCoding.SPAMS],
        [SklearnDL.DEFAULT_TRAINED_MODEL_FILENAME,
         SklearnDL.DEFAULT_TRAINED_MODEL_FILENAME,
         Spams.DEFAULT_TRAINED_MODEL_FILENAME,
         Spams.DEFAULT_TRAINED_MODEL_FILENAME],
        [JoachimsSVM.DEFAULT_MODEL_FILENAME,
         JoachimsSVM.DEFAULT_TRAINED_MODEL_FILENAME,
         JoachimsSVM.DEFAULT_MODEL_FILENAME,
         JoachimsSVM.DEFAULT_TRAINED_MODEL_FILENAME]):
        
        print message
        print feature_extraction_library_name
        print trained_feature_extraction_model_filename
        print classification_model_filename

        # get whitened patches
        whitened_patches_1 = test_whitening(image_filename_1, False, False)
        whitened_patches_2 = test_whitening(image_filename_2, False, False)

        # create sparse coding object
        print "loading trained feature extraction model from file :\n", trained_feature_extraction_model_filename
        sparse_coding = SparseCoding(feature_extraction_library_name,
                                     trained_feature_extraction_model_filename)

        # get pooled features directly from whitened patches using feature extraction pipeline
        pooled_features_1 = sparse_coding.get_pooled_features_from_whitened_patches(whitened_patches_1)
        pooled_features_2 = sparse_coding.get_pooled_features_from_whitened_patches(whitened_patches_2)

        # input X, flattened features, ndim = 2, [n_samples, n_features]. Here there is only one image, so n_samples = 1
        X_input_1 = pooled_features_1.ravel().reshape((1,-1)) # will be removed when pipeline has standardized shapes.
        X_input_2 = pooled_features_2.ravel().reshape((1,-1)) # will be removed when pipeline has standardized shapes.
        X_input = np.vstack((X_input_1,X_input_2))

        # generate an fake class Y for X, ndim = 1, [n_samples]
        Y_input = np.arange(X_input.shape[0])

        # create default JoachimsSVM object
        joachims_svm = JoachimsSVM()

        # training the JoachimsSVM on X and Y. This is just to train once for the JoachimsSVM to be able to classify.
        joachims_svm.train(X_input, Y_input)

        # save the model
        print "saving classification model to file :\n", classification_model_filename
        joachims_svm.save_model(classification_model_filename)

        # re-load the classification model
        print "re-loading classification model from file :\n", classification_model_filename
        joachims_svm = JoachimsSVM(model_filename=classification_model_filename)

        # predict the class of X
        Y_predict = joachims_svm.get_predictions(X_input)

        print "pooled features 1 shape :\n", pooled_features_1.shape
        print "pooled features 2 shape :\n", pooled_features_2.shape

        print "X_input shape :\n", X_input.shape

        print "Y_input shape :\n", Y_input.shape
        print "Y_input :\n", Y_input

        print "Y_predict shape :\n", Y_predict.shape
        print "Y_predict :\n", Y_predict

