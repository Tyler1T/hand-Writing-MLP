module neuron_layer1(data, bias, neuron, out);
    input logic [5:0] neuron;
    input logic [767:0] data[15:0];
    input logic [15:0] bias;
    output logic [15:0] out;

    logic [17:0] ra1;
    logic [15:0] weight;
    logic [15:0] sum;
    logic [15:0] temp;

    for(int i = 0; i < 768; i++){
        assign ra1 = {neuron, i};
        regfile_weight1 weight(ra1, weight);
        csam multiplier(temp, weight, data[i])
        CLA_with_BCLG16 adder(temp, pre, 1'b0, sum);
    }

    ReLU activation(sum, out);
endmodule // neuron

module neuron_layer2(data, bias, neuron, out);
    input logic [5:0] neuron;
    input logic [767:0] data[15:0];
    input logic [15:0] bias;
    output logic [15:0] out;

    logic [17:0] ra1;
    logic [15:0] weight;
    logic [15:0] sum;
    logic [15:0] temp;

    for(int i = 0; i < 768; i++){
        assign ra1 = {neuron, i};
        regfile_weight1 weight(ra1, weight);
        csam multiplier(temp, weight, data[i])
        CLA_with_BCLG16 adder(temp, pre, 1'b0, sum);
    }

    ReLU activation(sum, out);
endmodule // neuron

module neuron_layer3(data, bias, neuron, out);
    input logic [5:0] neuron;
    input logic [767:0] data[15:0];
    input logic [15:0] bias;
    output logic [15:0] out;

    logic [17:0] ra1;
    logic [15:0] weight;
    logic [15:0] sum;
    logic [15:0] temp;

    for(int i = 0; i < 768; i++){
        assign ra1 = {neuron, i};
        regfile_weight1 weight(ra1, weight);
        csam multiplier(temp, weight, data[i])
        CLA_with_BCLG16 adder(temp, pre, 1'b0, sum);
    }

    ReLU activation(sum, out);
endmodule // neuron
