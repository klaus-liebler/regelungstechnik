{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Sprungantwort einer PT2-Strecke"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 1500x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "880418368c0747a4bf18aacc93491def",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "interactive(children=(FloatSlider(value=1.0, description='T', max=4.0, min=0.5), IntSlider(value=1, descriptio…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "import matplotlib.pyplot as plt\n",
    "from ipywidgets import interact, interactive, fixed, interact_manual\n",
    "import numpy as np\n",
    "import scipy as sc\n",
    "import control\n",
    "\n",
    "plt.rcParams[\"figure.figsize\"] = (15,6)\n",
    "\n",
    "# animate plolspace?\n",
    "animate=True # True / False\n",
    "\n",
    "\n",
    "@interact(T=(0.5,4,0.1), N=(1,10,1))\n",
    "def f(T=1, N=1):\n",
    "    K=1\n",
    "    pt1 = control.TransferFunction([K], [T,1])\n",
    "    sys = control.TransferFunction([K], [T,1])\n",
    "    t, y = control.step_response(sys, T=20)\n",
    "    plt.plot(t, y)\n",
    "    for n in range(N-1):\n",
    "        sys =  control.series(sys, pt1)\n",
    "        t, y = control.step_response(sys, T=20)\n",
    "        plt.plot(t, y)\n",
    "\n",
    "    plt.xlabel('Time [s]')\n",
    "    plt.ylabel('Amplitude')\n",
    "    plt.title('Step response')\n",
    "    plt.grid()\n",
    "    plt.show()     \n",
    "    return;\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.6"
  },
  "vscode": {
   "interpreter": {
    "hash": "369f2c481f4da34e4445cda3fffd2e751bd1c4d706f27375911949ba6bb62e1c"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
