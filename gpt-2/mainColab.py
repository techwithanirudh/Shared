!git clone https://github.com/ilopezfr/gpt-2/
# import os
# os.chdir('gpt-2')
# !python download_model.py 345M 
# !python -m pip install flasgger
# !python -m pip install tensorflow==1.14
from google.colab.output import eval_js
print('URL: ' + eval_js('google.colab.kernel.proxyPort(5000)') + 'text-generate?input_text=once+upon+a+time+in+london&model_name=345M')
!python3 /content/gpt-2/src/flask_api_gpt2.py