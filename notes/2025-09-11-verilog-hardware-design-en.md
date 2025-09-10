---
title: Verilog for Hardware Design and Verification
date: 2025-09-11
lang: en
layout: post
audio: false
translated: false
generated: true
image: false
model: openai/gpt-5
---

Here’s a concise, comprehensive introduction to Verilog for digital hardware design and verification.

What Verilog is
- Verilog is a hardware description language (HDL) used to model, simulate, and synthesize digital systems (ASICs and FPGAs).
- It describes hardware structurally (gates/modules), at register-transfer level (RTL), and behaviorally (for testbenches).
- Standardized as IEEE 1364 (1995, 2001, 2005). SystemVerilog (IEEE 1800) is its successor, adding strong verification and richer RTL features. Most modern flows accept both.

Where it’s used in the design flow
- Architecture/specification
- RTL coding in Verilog
- Simulation (unit and system-level testbenches)
- Synthesis to gates, then place-and-route
- Static timing analysis (STA), gate-level simulation with SDF back-annotation
- Signoff and tape-out (ASIC) or bitstream generation (FPGA)

Core language concepts
- Concurrency: All modules and continuous assignments execute concurrently; procedural blocks are evaluated by the simulator’s event scheduler.
- 4-state logic: 0, 1, X (unknown), Z (high-impedance). X/Z propagate in simulation and help catch bugs.

Modules, ports, parameters, hierarchy
- module … endmodule defines a hardware block with inputs/outputs.
- Ports can be scalar or vectors [msb:lsb].
- Parameters customize modules at instantiation time.
- Modules are instantiated hierarchically.

Example: parameterized adder (synthesizable)
module add #(parameter W=8) (
  input  [W-1:0] a, b,
  output [W:0]   sum
);
  assign sum = a + b;
endmodule

Data types and nets
- Nets (wire, tri, wand, wor) represent connections; driven by continuous assignments or module outputs.
- Reg represents storage in procedural blocks (doesn’t imply a flop unless clocked logic is used).
- Integer, time, real exist but are generally non-synthesizable (or used only for constants/sim).
- Signed vs unsigned: vectors are unsigned by default; declare signed if needed: reg signed [15:0] a;

Operators
- Arithmetic: + - * / % (beware synthesis support and widths)
- Bitwise: ~ & | ^ ^~ (xnor)
- Logical: ! && ||
- Reduction: & | ^ ~& ~| ~^
- Shifts: << >> (arithmetic shift >>> in newer versions)
- Concatenation: {a,b}, replication: {4{1’b0}}

Assignments and processes
- Continuous assignment: assign y = a & b; drives nets continuously (combinational).
- Procedural blocks:
  - initial: simulation-only initialization/sequencing
  - always: repeated process, sensitive to signals/events
- Sensitivity:
  - Combinational: always @* (Verilog-2001) or always @(a or b or c)
  - Sequential: always @(posedge clk [or negedge rst_n])
- Blocking (=) vs non-blocking (<=):
  - Use non-blocking (<=) in clocked sequential logic to avoid races.
  - Use blocking (=) for combinational logic inside an always @*.
  - Never assign the same reg with both kinds in the same time step.

Examples: counter and combinational logic
module counter #(parameter W=8) (
  input              clk,
  input              rst_n,     // active-low async reset
  input              en,
  output reg [W-1:0] q
);
  always @(posedge clk or negedge rst_n) begin
    if (!rst_n) q <= {W{1'b0}};
    else if (en) q <= q + 1'b1;
  end
endmodule

module mux2 (
  input  [7:0] a, b,
  input        sel,
  output reg [7:0] y
);
  always @* begin
    y = a;
    if (sel) y = b;
  end
endmodule

Control logic and FSMs
- Use a two-process style: one sequential block for the state register, one combinational block for next-state and outputs.
- Provide defaults in the combinational block to avoid inferring latches.

Example: simple FSM
module fsm (
  input        clk, rst_n, start, done,
  output reg   busy
);
  localparam S_IDLE=2'd0, S_RUN=2'd1, S_DONE=2'd2;
  reg [1:0] state, next_state;

  always @(posedge clk or negedge rst_n) begin
    if (!rst_n) state <= S_IDLE;
    else        state <= next_state;
  end

  always @* begin
    next_state = state;
    busy = 1'b0;
    case (state)
      S_IDLE: if (start) next_state = S_RUN;
      S_RUN:  begin busy = 1'b1; if (done) next_state = S_DONE; end
      S_DONE: next_state = S_IDLE;
      default: next_state = S_IDLE;
    endcase
  end
endmodule

Generate and parameterization
- Generate synthesizable repetition/conditional structure at elaboration time.

Example: bitwise AND with enable
module and_en #(parameter N=8) (
  input  [N-1:0] a,
  input          en,
  output [N-1:0] y
);
  genvar i;
  generate
    for (i=0; i<N; i=i+1) begin : g
      assign y[i] = a[i] & en;
    end
  endgenerate
endmodule

Memory modeling and inference
- ROM/RAM inference depends on the coding template and the synthesis tool.

Example: single-port RAM (common inference)
module spram #(parameter AW=8, DW=8) (
  input                clk,
  input                we,
  input      [AW-1:0]  addr,
  input      [DW-1:0]  din,
  output reg [DW-1:0]  dout
);
  reg [DW-1:0] mem [0:(1<<AW)-1];

  always @(posedge clk) begin
    if (we) mem[addr] <= din;
    dout <= mem[addr];
  end
endmodule

- Testbenches can initialize memories: initial $readmemh("init.hex", mem);

Testbenches and simulation-only features
- Testbench constructs are not synthesizable: initial blocks, delays (#), $display/$monitor, $time, $finish, $random, $dumpvars.
- Use tasks/functions to structure stimulus and checking.

Minimal testbench example
`timescale 1ns/1ps
`default_nettype none
module tb_counter;
  reg clk = 0;
  always #5 clk = ~clk;  // 100 MHz

  reg rst_n = 0, en = 0;
  wire [7:0] q;

  counter #(8) dut (.clk(clk), .rst_n(rst_n), .en(en), .q(q));

  initial begin
    $dumpfile("waves.vcd");
    $dumpvars(0, tb_counter);
    #20  rst_n = 1;
    #30  en = 1;
    repeat (20) @(posedge clk);
    $display("q=%0d", q);
    $finish;
  end
endmodule
`default_nettype wire

Timing, delays, and back-annotation
- RTL should avoid #delays; they’re for testbenches and behavioral modeling.
- Specify blocks and SDF back-annotation apply post-synthesis/place-and-route for gate-level timing simulation.

Preprocessor and file organization
- `define, `include, `ifdef/`ifndef used for macros, compilation switches (e.g., `ifdef SYNTHESIS).
- `timescale sets time unit/precision for delays in that compilation unit.
- Best practice: begin RTL files with `default_nettype none to forbid implicit nets; restore with `default_nettype wire at file end.

Synthesis-friendly coding guidelines
- One clock per always block; non-blocking (<=) in sequential logic; blocking (=) in combinational logic.
- Always assign all outputs in combinational blocks (give defaults) to avoid latches.
- Avoid #delays, wait, fork-join, file I/O, and most $system tasks in RTL.
- Prefer localparam for state encodings/constants; avoid defparam.
- Use explicit widths and signedness; match port widths; cast when needed.
- Resets: choose async or sync consistently; ensure proper reset of flops that need known power-up values.
- Tri-states are usually only at top-level I/O; FPGAs map internal tri-states to muxes.
- Clock-domain crossing needs synchronizers/FIFOs; don’t cross domains with raw signals.

Common pitfalls
- Implicit nets: a misspelled signal silently creates wire [0:0]; prevent with `default_nettype none.
- Blocking vs non-blocking races: mixing incorrectly leads to simulation/synthesis mismatches.
- Incomplete sensitivity list (pre-2001): use always @* to avoid missed updates.
- Latch inference: missing else/default in combinational logic.
- casex/casez: X/Z masking can hide real bugs; use carefully and include default.
- X-propagation differences in sim vs hardware power-up state: explicitly reset what matters.
- Width mismatches and signed math: be explicit to avoid truncation/overflow surprises.

Tooling
- Simulators: Icarus Verilog (open-source), Verilator (fast cycle-accurate, lint), ModelSim/Questa (Siemens), VCS (Synopsys), Xcelium (Cadence).
- Synthesis: Yosys (open-source), Vivado (AMD/Xilinx), Quartus (Intel), Libero (Microchip), Synopsys DC, Cadence Genus.
- Lint/format: Verilator, Verible.
- Waveform viewers: GTKWave, commercial viewers.

When to consider SystemVerilog
- For modern RTL: logic type (replaces reg/wire confusion), always_ff/always_comb, enumerated types, packed arrays, interfaces, assertions, constrained random, functional coverage, classes for UVM. Most shops use SystemVerilog for both design and verification today.

Learning path
- Start with simple combinational and sequential modules.
- Build self-checking testbenches and run simulations.
- Learn synthesis templates for memories and FSMs.
- Add parameterization and generate constructs.
- Practice CDC, resets, and timing-friendly RTL.
- Use linting and unit tests in your CI.

If you want, I can provide a small project scaffold (RTL + testbench + Makefile) that runs with open-source tools to get you hands-on quickly.