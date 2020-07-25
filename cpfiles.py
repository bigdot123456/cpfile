import os
import shutil
import sys

m0list = {}
m0list["rtl/inc"] = ["../verilog/cortex_m0_mcu_defs.v",
                     "../../../logical/models/memories/ahb_memory_models_defs.v",
                     "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0_dap/verilog/cm0_dap_dp_sw_defs.v",
                     "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0_dap/verilog/cm0_dap_dp_jtag_defs.v",
                     "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0_dap/verilog/cm0_dap_ap_mast_defs.v",
                     "../../../logical/apb_dualtimers/verilog/apb_dualtimers_defs.v",
                     "../../../logical/apb_watchdog/verilog/apb_watchdog_defs.v"
                     ]
m0list["tb/debug_tester"] = [
    "../debug_tester/verilog/cortexm0_debug_tester.v",
    "../debug_tester/verilog/cortexm0_debug_tester_rom.v",
    "../debug_tester/verilog/cortexm0_debug_tester_ahb_sram_bridge.v",
    "../debug_tester/verilog/cortexm0_debug_tester_sram.v",
    "../debug_tester/verilog/cortexm0_debug_tester_ahb_interconnect.v",
    "../debug_tester/verilog/cortexm0_debug_tester_ahb_def_slv.v",
    "../debug_tester/verilog/cortexm0_debug_tester_io.v",
]

m0list["tb"] = [
    "../verilog/tb_clkreset.v",
    "../verilog/tb_uart_capture.v",
]

m0list["rtl/m0_mcu"] = ["../verilog/cortex_m0_mcu.v"]

m0list["rtl/m0"] = [
    "../verilog/cortex_m0_mcu_clkctrl.v",
    "../verilog/cortex_m0_mcu_system.v",
    "../verilog/cortex_m0_mcu_pin_mux.v",
    "../verilog/cortex_m0_mcu_sysctrl.v",
    "../verilog/cortex_m0_mcu_stclkctrl.v",
]

m0list["mem"] = [
    "../../../logical/models/clkgate/mcu_clock_gate.v",
    "../../../logical/models/memories//ahb_rom.v",
    "../../../logical/models/memories//ahb_ram.v",
    "../../../logical/models/memories//ahb_ram_beh.v",
    "../../../logical/models/memories//fpga_rom.v",
    "../../../logical/models/memories//flash_rom32.v",
    "../../../logical/models/memories//fpga_sram.v",
    "../../../logical/models/memories//sram256x16.v",
    "../../../logical/models/memories//sram256x8.v",
]

m0list["rtl/amba"] = [
    "../../../logical/apb_subsystem/verilog/apb_subsystem.v",
    "../../../logical/apb_subsystem/verilog/apb_test_slave.v",
    "../../../logical/apb_subsystem/verilog/irq_sync.v",
    "../../../logical/ahb_slave_mux/verilog/ahb_slave_mux.v",
    "../../../logical/ahb_master_mux/verilog/ahb_master_mux.v",
    "../../../logical/ahb_default_slave/verilog/ahb_default_slave.v",
    "../../../logical/ahb_gpio/verilog/ahb_gpio.v",
    "../../../logical/ahb_to_apb/verilog/ahb_to_apb.v",
    "../../../logical/ahb_bitband/verilog/ahb_bitband.v",
    "../../../logical/ahb_to_sram/verilog/ahb_to_sram.v",
    "../../../logical/ahb_to_flash32/verilog/ahb_to_flash32.v",
    "../../../logical/ahb_to_extmem16/verilog/ahb_to_extmem16.v",
    "../../../logical/ahb_to_extmem16/verilog/ahb_to_extmem16_ahb_fsm.v",
    "../../../logical/ahb_to_extmem16/verilog/ahb_to_extmem16_mem_fsm.v",
]
# Peripherals.
m0list["rtl/m0perip"] = [
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0_integration/verilog/CORTEXM0INTEGRATION.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0_integration/verilog/cortexm0_pmu.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0_integration/verilog/cortexm0_wic.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/models/cells/cm0_dbg_reset_sync.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/models/cells/cm0_pmu_sync_set.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/models/cells/cm0_pmu_sync_reset.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/models/cells/cm0_pmu_cdc_send_reset.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/models/cells/cm0_pmu_cdc_send_set.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/models/cells/cm0_pmu_acg.v",
    "../../../logical/apb_timer/verilog/apb_timer.v",
    "../../../logical/apb_dualtimers/verilog/apb_dualtimers.v",
    "../../../logical/apb_dualtimers/verilog/apb_dualtimers_frc.v",
    "../../../logical/apb_uart/verilog/apb_uart.v",
    "../../../logical/apb_watchdog/verilog/apb_watchdog.v",
    "../../../logical/apb_watchdog/verilog/apb_watchdog_frc.v",
    "../../../logical/apb_slave_mux/verilog/apb_slave_mux.v",
]

m0list["rtl/m0core"] = [
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0/verilog/CORTEXM0.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0/verilog/cm0_top.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0/verilog/cm0_top_sys.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0/verilog/cm0_top_dbg.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0/verilog/cm0_top_clk.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0/verilog/cm0_core.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0/verilog/cm0_nvic.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0/verilog/cm0_matrix.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0/verilog/cm0_dbg_ctl.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0/verilog/cm0_dbg_bpu.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0/verilog/cm0_dbg_dwt.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0/verilog/cm0_dbg_if.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0/verilog/cm0_dbg_sel.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0/verilog/cm0_core_alu.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0/verilog/cm0_core_spu.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0/verilog/cm0_core_mul.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0/verilog/cm0_core_psr.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0/verilog/cm0_core_gpr.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0/verilog/cm0_core_pfu.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0/verilog/cm0_core_ctl.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0/verilog/cm0_nvic_reg.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0/verilog/cm0_nvic_main.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0/verilog/cm0_matrix_sel.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0/verilog/cm0_core_dec.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0_dap/verilog/CORTEXM0DAP.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0_dap/verilog/cm0_dap_dp.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0_dap/verilog/cm0_dap_ap.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0_dap/verilog/cm0_dap_dp_jtag.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0_dap/verilog/cm0_dap_dp_sw.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0_dap/verilog/cm0_dap_dp_cdc.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0_dap/verilog/cm0_dap_dp_pwr.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0_dap/verilog/cm0_dap_ap_mast.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/cortexm0_dap/verilog/cm0_dap_ap_cdc.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/models/cells/cm0_acg.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/models/cells/cm0_dap_jt_cdc_comb_and.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/models/cells/cm0_dap_sw_cdc_capt_reset.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/models/cells/cm0_dap_cdc_capt_sync.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/models/cells/cm0_dap_cdc_send_reset.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/models/cells/cm0_dap_cdc_send_data.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/models/cells/cm0_dap_cdc_send_addr.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/models/cells/cm0_dap_cdc_send.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/models/cells/cm0_dap_cdc_comb_and_data.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/models/cells/cm0_dap_cdc_comb_and.v",
    "../../../cores/AT510-BU-50000-r0p0-02rel0/logical/models/cells/cm0_dap_cdc_comb_and_addr.v",
]

Filelist = []

for i in m0list.keys():
    if not os.path.exists(i):
        os.makedirs(i)
    rtlList = m0list[i]
    for j in rtlList:
        print(f"cp {j} {i}\n")
        # adding exception handling
        try:
            shutil.copy(j, i)
        except IOError as e:
            print("Unable to copy file. %s" % e)
        except:
            print("Unexpected error:", sys.exc_info())

    for home, dirs, files in os.walk(i):
        for filename in files:
            # 文件名列表，包含完整路径
            Filelist.append(os.path.join(home, filename))
            # # 文件名列表，只包含文件名
            # Filelist.append( filename)

# reduce repeated items
Filelist = list(set(Filelist))
Filelist.sort()
print(f"{Filelist}")

with open('./rtllist.f', 'w') as f:
    # f.write(f"{Filelist}\n")
    for i in Filelist:
        f.write(f"{i}\n")

# +libext+.v+.vlib
# +incdir+../verilog/
with open('./rtlinc.f', 'w') as f:
    f.write(f"+libext+.v+.vlib -sv\n")
    for i in m0list.keys():
        f.write(f"+incdir+{i}\n")
