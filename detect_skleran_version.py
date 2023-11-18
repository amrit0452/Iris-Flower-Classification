import pickle
import sklearn
import warnings
from sklearn.exceptions import InconsistentVersionWarning

warnings.simplefilter("error", InconsistentVersionWarning)

try:
    model = pickle.load(open('saved_model1.pkl','rb'))
except InconsistentVersionWarning as w:
    print(w.original_sklearn_version)