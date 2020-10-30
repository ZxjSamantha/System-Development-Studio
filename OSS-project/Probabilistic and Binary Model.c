#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float SigmoidF(double sum){
    float return_value;

    return_value = 1/(1+exp(0-sum));

    return return_value;
}

float WeightedSum(float *arrX, float *arrW, int inputSize, int neuronSize){
    int i;
    double sum = 0.0;

    for (i=0; i<inputSize; i++){
        sum += (*(arrX+i)) * (*(arrW+i));
    }

    return sum; 
}

float perceptron(float *inputs, float *weights, int inputSize, int neuronSize){
    double sum;
    float output;
    float WeightedSum(float *, float*, int, int);
    float SigmoidF(double);

    sum = WeightedSum(inputs, weights, inputSize, neuronSize);
    output = SigmoidF(sum);
    printf("Output of Neuron is %.2f\n", output);

    return output;
}

int main(){
    int inputSize = 10;
    int neuronSize = 10;
    int rollDie = 10000; 
    float p;
    float testNumber = RAND_MAX * p;
    float inputs[inputSize];
    float weights[neuronSize];
    float y[rollDie];
    int i;
    int counter = 0;
    int time();
    

    srand(time(0));

    // Generate inputs
    for(i=0; i<inputSize; i++){
        inputs[i] = 0 + 1.0*(rand()%RAND_MAX)/RAND_MAX*(1-0);
        //printf("Input %d is %.2f \n", i, inputs[i]);
    }

    for(i=0; i<neuronSize; i++){
        weights[i] = 0 + 1.0*(rand()%RAND_MAX)/RAND_MAX*(1-0);
        //printf("Input %d is %.2f \n", i, weights[i]);
    }

    p = perceptron(inputs, weights, inputSize, neuronSize);
    printf("The probability is %.2f \n", p);

    //for(i=0; i<rollDie;i++){
    //    if(inputs[])
    //}

    for(i=0; i<size; i++){
        inputs[i] = 0+1.0*(rand()%RAND_MAX)/RAND_MAX*(1-0); generate random number in [0,1]
       
        if (inputs[i] <= testNumber){
            y[i] = 1;
            counter++; 
        }
        else
        {
            y[i] = 0;
        }
        

    }
    for(i=0; i<size;i++){
        printf("Result is %.5f \n", y[i]);
    }
    printf("The times of y == 1 is %d \n", counter);

    return 0;
}
