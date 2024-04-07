import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline


class Histogram:
    def __init__(self, X, decimal_points=None):
        self.X = np.sort(X)
        self.n = len(X)
        self.__decimal = 2 if decimal_points is None else decimal_points
        self.number_of_classes = int(round(3.3*np.log10(self.n)+1, 0))
        self.amplitude = self.X[-1]-self.X[0]
        self.aritmetic_mean = np.sum(self.X)/self.n
        self.__class_width = round(self.amplitude/self.number_of_classes, self.__decimal)  
    

    def __calc_class_limits(self):
             
        excess = round(self.X[0]+self.number_of_classes*self.__class_width-self.X[-1], self.__decimal)
        if excess == 0:
            # Mantém o limite inicial de classe 
            class_init = self.X[0]           
        else:
            # Ajusta o limite inicial de classe para X[0]-excesso
            class_init = round(self.X[0]-excess/2, self.__decimal)
        
        class_end = round(class_init+self.__class_width, self.__decimal)

        c_limits = []  
        for _ in range(self.number_of_classes):
            c_limits.append(tuple((class_init, class_end)))
            class_init = round(class_end, self.__decimal)
            class_end = round(class_init+self.__class_width,self.__decimal)
        
        return c_limits


    def __class_frequencies(self):
        class_limits = self.__calc_class_limits()
        class_freqs = [0]*self.number_of_classes
  
        for element in self.X:
            for i in range(self.number_of_classes):
                if class_limits[i][0] <= element < class_limits[i][1]:
                    class_freqs[i]+=1
   
        return class_freqs
    

    def __relative_frequencies(self):
        freqs=np.array(self.__class_frequencies())
        return list(
            np.round(
                (freqs/self.n),self.__decimal)
                )

    def __cumulative_frequencies(self):
        freqs=self.__class_frequencies()
        cum_freqs=[freqs[0]]

        for i in range((self.number_of_classes)-1):
            cum_freqs.append(cum_freqs[i]+freqs[i+1])
     
        return cum_freqs
    

    def frequency_table(self):
        tb={
            "Classes": self.__calc_class_limits(),
            "Frequency": self.__class_frequencies(),
            "rFrequency": self.__relative_frequencies(),
            "cFrequency": self.__cumulative_frequencies()
            }
        
        return pd.DataFrame(tb)
    

    def show(self):
        plt.bar([str(x) for x in self.__calc_class_limits()], self.__class_frequencies(),
                width=.99,
                align='center',
                color='Green')
        plt.xticks(rotation=90)
        plt.show()



if __name__=="__main__":
    colesterol = np.array([140,160,168,180,180,180,180,184,185,190,
                       190,192,192,196,200,200,200,205,205,208,
                       214,214,220,220,225,230,240,260,280,315])
    hist=Histogram(colesterol)
    print(hist.frequency_table())
    hist.show()
        