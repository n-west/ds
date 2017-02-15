#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Receive Single FM Station
# Author: Nathan West
# Generated: Wed Feb 15 14:55:17 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys
import time


class rcv_single_fm(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Receive Single FM Station")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Receive Single FM Station")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "rcv_single_fm")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.rf_rate = rf_rate = 20e6
        self.rf_frequency_h = rf_frequency_h = 88.5
        self.fm_taps = fm_taps = firdes.low_pass_2(32., rf_rate, 96e3, 25e3, 50)
        self.audio_rate = audio_rate = 44100
        self.taps_len = taps_len = fm_taps.__len__()
        self.rf_gain = rf_gain = 50
        self.rf_frequency = rf_frequency = 98.1e6
        self.fm_channel_rate = fm_channel_rate = audio_rate*5
        self.channel_number = channel_number = int(10*(rf_frequency_h-98)) /2if rf_frequency_h>=98 else 50 + int(10*(rf_frequency_h-88.1))/2

        ##################################################
        # Blocks
        ##################################################
        self._rf_rate_range = Range(100e3, 20e6, 200e3, 20e6, 200)
        self._rf_rate_win = RangeWidget(self._rf_rate_range, self.set_rf_rate, 'RF sample rate', "counter_slider", float)
        self.top_layout.addWidget(self._rf_rate_win)
        self._rf_gain_range = Range(0, 90, 1, 50, 200)
        self._rf_gain_win = RangeWidget(self._rf_gain_range, self.set_rf_gain, 'RF gain', "counter_slider", float)
        self.top_layout.addWidget(self._rf_gain_win)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(rf_rate)
        self.uhd_usrp_source_0.set_center_freq(rf_frequency, 0)
        self.uhd_usrp_source_0.set_gain(rf_gain, 0)
        self.uhd_usrp_source_0.set_antenna('RX2', 0)
        self._rf_frequency_h_range = Range(88.0, 108.0, .2, 88.5, 200)
        self._rf_frequency_h_win = RangeWidget(self._rf_frequency_h_range, self.set_rf_frequency_h, 'RF Frequency', "counter_slider", float)
        self.top_layout.addWidget(self._rf_frequency_h_win)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=fm_channel_rate,
                decimation=int(200e3),
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_waterfall_sink_x_0_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rf_frequency, #fc
        	rf_rate, #bw
        	"Received Spectrum", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_0.enable_axis_labels(True)
        
        if not True:
          self.qtgui_waterfall_sink_x_0_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0_0.set_plot_pos_half(not True)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self.qtgui_waterfall_sink_x_0_0.set_intensity_range(-140, 10)
        
        self._qtgui_waterfall_sink_x_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_0_win)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rf_frequency, #fc
        	fm_channel_rate, #bw
        	"Selected Channel", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)
        
        if not True:
          self.qtgui_waterfall_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])
        
        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)
        
        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	1., #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.pfb_channelizer_ccf_0 = pfb.channelizer_ccf(
        	  100,
        	  (fm_taps),
        	  1.0,
        	  100)
        self.pfb_channelizer_ccf_0.set_channel_map(([channel_number]))
        self.pfb_channelizer_ccf_0.declare_sample_delay(0)
        	
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.audio_sink_0 = audio.sink(audio_rate, '', True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=fm_channel_rate,
        	audio_decimation=fm_channel_rate/audio_rate,
        )
        self.analog_simple_squelch_cc_0 = analog.simple_squelch_cc(-20, .1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_simple_squelch_cc_0, 0), (self.analog_wfm_rcv_0, 0))    
        self.connect((self.analog_wfm_rcv_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.pfb_channelizer_ccf_0, 1), (self.blocks_null_sink_0, 0))    
        self.connect((self.pfb_channelizer_ccf_0, 2), (self.blocks_null_sink_0, 1))    
        self.connect((self.pfb_channelizer_ccf_0, 3), (self.blocks_null_sink_0, 2))    
        self.connect((self.pfb_channelizer_ccf_0, 4), (self.blocks_null_sink_0, 3))    
        self.connect((self.pfb_channelizer_ccf_0, 5), (self.blocks_null_sink_0, 4))    
        self.connect((self.pfb_channelizer_ccf_0, 6), (self.blocks_null_sink_0, 5))    
        self.connect((self.pfb_channelizer_ccf_0, 7), (self.blocks_null_sink_0, 6))    
        self.connect((self.pfb_channelizer_ccf_0, 8), (self.blocks_null_sink_0, 7))    
        self.connect((self.pfb_channelizer_ccf_0, 9), (self.blocks_null_sink_0, 8))    
        self.connect((self.pfb_channelizer_ccf_0, 10), (self.blocks_null_sink_0, 9))    
        self.connect((self.pfb_channelizer_ccf_0, 11), (self.blocks_null_sink_0, 10))    
        self.connect((self.pfb_channelizer_ccf_0, 12), (self.blocks_null_sink_0, 11))    
        self.connect((self.pfb_channelizer_ccf_0, 13), (self.blocks_null_sink_0, 12))    
        self.connect((self.pfb_channelizer_ccf_0, 14), (self.blocks_null_sink_0, 13))    
        self.connect((self.pfb_channelizer_ccf_0, 15), (self.blocks_null_sink_0, 14))    
        self.connect((self.pfb_channelizer_ccf_0, 16), (self.blocks_null_sink_0, 15))    
        self.connect((self.pfb_channelizer_ccf_0, 17), (self.blocks_null_sink_0, 16))    
        self.connect((self.pfb_channelizer_ccf_0, 18), (self.blocks_null_sink_0, 17))    
        self.connect((self.pfb_channelizer_ccf_0, 19), (self.blocks_null_sink_0, 18))    
        self.connect((self.pfb_channelizer_ccf_0, 20), (self.blocks_null_sink_0, 19))    
        self.connect((self.pfb_channelizer_ccf_0, 21), (self.blocks_null_sink_0, 20))    
        self.connect((self.pfb_channelizer_ccf_0, 22), (self.blocks_null_sink_0, 21))    
        self.connect((self.pfb_channelizer_ccf_0, 23), (self.blocks_null_sink_0, 22))    
        self.connect((self.pfb_channelizer_ccf_0, 24), (self.blocks_null_sink_0, 23))    
        self.connect((self.pfb_channelizer_ccf_0, 25), (self.blocks_null_sink_0, 24))    
        self.connect((self.pfb_channelizer_ccf_0, 26), (self.blocks_null_sink_0, 25))    
        self.connect((self.pfb_channelizer_ccf_0, 27), (self.blocks_null_sink_0, 26))    
        self.connect((self.pfb_channelizer_ccf_0, 28), (self.blocks_null_sink_0, 27))    
        self.connect((self.pfb_channelizer_ccf_0, 29), (self.blocks_null_sink_0, 28))    
        self.connect((self.pfb_channelizer_ccf_0, 30), (self.blocks_null_sink_0, 29))    
        self.connect((self.pfb_channelizer_ccf_0, 31), (self.blocks_null_sink_0, 30))    
        self.connect((self.pfb_channelizer_ccf_0, 32), (self.blocks_null_sink_0, 31))    
        self.connect((self.pfb_channelizer_ccf_0, 33), (self.blocks_null_sink_0, 32))    
        self.connect((self.pfb_channelizer_ccf_0, 34), (self.blocks_null_sink_0, 33))    
        self.connect((self.pfb_channelizer_ccf_0, 35), (self.blocks_null_sink_0, 34))    
        self.connect((self.pfb_channelizer_ccf_0, 36), (self.blocks_null_sink_0, 35))    
        self.connect((self.pfb_channelizer_ccf_0, 37), (self.blocks_null_sink_0, 36))    
        self.connect((self.pfb_channelizer_ccf_0, 38), (self.blocks_null_sink_0, 37))    
        self.connect((self.pfb_channelizer_ccf_0, 39), (self.blocks_null_sink_0, 38))    
        self.connect((self.pfb_channelizer_ccf_0, 40), (self.blocks_null_sink_0, 39))    
        self.connect((self.pfb_channelizer_ccf_0, 41), (self.blocks_null_sink_0, 40))    
        self.connect((self.pfb_channelizer_ccf_0, 42), (self.blocks_null_sink_0, 41))    
        self.connect((self.pfb_channelizer_ccf_0, 43), (self.blocks_null_sink_0, 42))    
        self.connect((self.pfb_channelizer_ccf_0, 44), (self.blocks_null_sink_0, 43))    
        self.connect((self.pfb_channelizer_ccf_0, 45), (self.blocks_null_sink_0, 44))    
        self.connect((self.pfb_channelizer_ccf_0, 46), (self.blocks_null_sink_0, 45))    
        self.connect((self.pfb_channelizer_ccf_0, 47), (self.blocks_null_sink_0, 46))    
        self.connect((self.pfb_channelizer_ccf_0, 48), (self.blocks_null_sink_0, 47))    
        self.connect((self.pfb_channelizer_ccf_0, 49), (self.blocks_null_sink_0, 48))    
        self.connect((self.pfb_channelizer_ccf_0, 50), (self.blocks_null_sink_0, 49))    
        self.connect((self.pfb_channelizer_ccf_0, 51), (self.blocks_null_sink_0, 50))    
        self.connect((self.pfb_channelizer_ccf_0, 52), (self.blocks_null_sink_0, 51))    
        self.connect((self.pfb_channelizer_ccf_0, 53), (self.blocks_null_sink_0, 52))    
        self.connect((self.pfb_channelizer_ccf_0, 54), (self.blocks_null_sink_0, 53))    
        self.connect((self.pfb_channelizer_ccf_0, 55), (self.blocks_null_sink_0, 54))    
        self.connect((self.pfb_channelizer_ccf_0, 56), (self.blocks_null_sink_0, 55))    
        self.connect((self.pfb_channelizer_ccf_0, 57), (self.blocks_null_sink_0, 56))    
        self.connect((self.pfb_channelizer_ccf_0, 58), (self.blocks_null_sink_0, 57))    
        self.connect((self.pfb_channelizer_ccf_0, 59), (self.blocks_null_sink_0, 58))    
        self.connect((self.pfb_channelizer_ccf_0, 60), (self.blocks_null_sink_0, 59))    
        self.connect((self.pfb_channelizer_ccf_0, 61), (self.blocks_null_sink_0, 60))    
        self.connect((self.pfb_channelizer_ccf_0, 62), (self.blocks_null_sink_0, 61))    
        self.connect((self.pfb_channelizer_ccf_0, 63), (self.blocks_null_sink_0, 62))    
        self.connect((self.pfb_channelizer_ccf_0, 64), (self.blocks_null_sink_0, 63))    
        self.connect((self.pfb_channelizer_ccf_0, 65), (self.blocks_null_sink_0, 64))    
        self.connect((self.pfb_channelizer_ccf_0, 66), (self.blocks_null_sink_0, 65))    
        self.connect((self.pfb_channelizer_ccf_0, 67), (self.blocks_null_sink_0, 66))    
        self.connect((self.pfb_channelizer_ccf_0, 68), (self.blocks_null_sink_0, 67))    
        self.connect((self.pfb_channelizer_ccf_0, 69), (self.blocks_null_sink_0, 68))    
        self.connect((self.pfb_channelizer_ccf_0, 70), (self.blocks_null_sink_0, 69))    
        self.connect((self.pfb_channelizer_ccf_0, 71), (self.blocks_null_sink_0, 70))    
        self.connect((self.pfb_channelizer_ccf_0, 72), (self.blocks_null_sink_0, 71))    
        self.connect((self.pfb_channelizer_ccf_0, 73), (self.blocks_null_sink_0, 72))    
        self.connect((self.pfb_channelizer_ccf_0, 74), (self.blocks_null_sink_0, 73))    
        self.connect((self.pfb_channelizer_ccf_0, 75), (self.blocks_null_sink_0, 74))    
        self.connect((self.pfb_channelizer_ccf_0, 76), (self.blocks_null_sink_0, 75))    
        self.connect((self.pfb_channelizer_ccf_0, 77), (self.blocks_null_sink_0, 76))    
        self.connect((self.pfb_channelizer_ccf_0, 78), (self.blocks_null_sink_0, 77))    
        self.connect((self.pfb_channelizer_ccf_0, 79), (self.blocks_null_sink_0, 78))    
        self.connect((self.pfb_channelizer_ccf_0, 80), (self.blocks_null_sink_0, 79))    
        self.connect((self.pfb_channelizer_ccf_0, 81), (self.blocks_null_sink_0, 80))    
        self.connect((self.pfb_channelizer_ccf_0, 82), (self.blocks_null_sink_0, 81))    
        self.connect((self.pfb_channelizer_ccf_0, 83), (self.blocks_null_sink_0, 82))    
        self.connect((self.pfb_channelizer_ccf_0, 84), (self.blocks_null_sink_0, 83))    
        self.connect((self.pfb_channelizer_ccf_0, 85), (self.blocks_null_sink_0, 84))    
        self.connect((self.pfb_channelizer_ccf_0, 86), (self.blocks_null_sink_0, 85))    
        self.connect((self.pfb_channelizer_ccf_0, 87), (self.blocks_null_sink_0, 86))    
        self.connect((self.pfb_channelizer_ccf_0, 88), (self.blocks_null_sink_0, 87))    
        self.connect((self.pfb_channelizer_ccf_0, 89), (self.blocks_null_sink_0, 88))    
        self.connect((self.pfb_channelizer_ccf_0, 90), (self.blocks_null_sink_0, 89))    
        self.connect((self.pfb_channelizer_ccf_0, 91), (self.blocks_null_sink_0, 90))    
        self.connect((self.pfb_channelizer_ccf_0, 92), (self.blocks_null_sink_0, 91))    
        self.connect((self.pfb_channelizer_ccf_0, 93), (self.blocks_null_sink_0, 92))    
        self.connect((self.pfb_channelizer_ccf_0, 94), (self.blocks_null_sink_0, 93))    
        self.connect((self.pfb_channelizer_ccf_0, 95), (self.blocks_null_sink_0, 94))    
        self.connect((self.pfb_channelizer_ccf_0, 96), (self.blocks_null_sink_0, 95))    
        self.connect((self.pfb_channelizer_ccf_0, 97), (self.blocks_null_sink_0, 96))    
        self.connect((self.pfb_channelizer_ccf_0, 98), (self.blocks_null_sink_0, 97))    
        self.connect((self.pfb_channelizer_ccf_0, 99), (self.blocks_null_sink_0, 98))    
        self.connect((self.pfb_channelizer_ccf_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_simple_squelch_cc_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_waterfall_sink_x_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.pfb_channelizer_ccf_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_waterfall_sink_x_0_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "rcv_single_fm")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_rf_rate(self):
        return self.rf_rate

    def set_rf_rate(self, rf_rate):
        self.rf_rate = rf_rate
        self.set_fm_taps(firdes.low_pass_2(32., self.rf_rate, 96e3, 25e3, 50))
        self.uhd_usrp_source_0.set_samp_rate(self.rf_rate)
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(self.rf_frequency, self.rf_rate)

    def get_rf_frequency_h(self):
        return self.rf_frequency_h

    def set_rf_frequency_h(self, rf_frequency_h):
        self.rf_frequency_h = rf_frequency_h
        self.set_channel_number(int(10*(self.rf_frequency_h-98)) /2if self.rf_frequency_h>=98 else 50 + int(10*(self.rf_frequency_h-88.1))/2)

    def get_fm_taps(self):
        return self.fm_taps

    def set_fm_taps(self, fm_taps):
        self.fm_taps = fm_taps
        self.pfb_channelizer_ccf_0.set_taps((self.fm_taps))

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate
        self.set_fm_channel_rate(self.audio_rate*5)

    def get_taps_len(self):
        return self.taps_len

    def set_taps_len(self, taps_len):
        self.taps_len = taps_len

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain
        self.uhd_usrp_source_0.set_gain(self.rf_gain, 0)
        	

    def get_rf_frequency(self):
        return self.rf_frequency

    def set_rf_frequency(self, rf_frequency):
        self.rf_frequency = rf_frequency
        self.uhd_usrp_source_0.set_center_freq(self.rf_frequency, 0)
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(self.rf_frequency, self.rf_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rf_frequency, self.fm_channel_rate)

    def get_fm_channel_rate(self):
        return self.fm_channel_rate

    def set_fm_channel_rate(self, fm_channel_rate):
        self.fm_channel_rate = fm_channel_rate
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rf_frequency, self.fm_channel_rate)

    def get_channel_number(self):
        return self.channel_number

    def set_channel_number(self, channel_number):
        self.channel_number = channel_number
        self.pfb_channelizer_ccf_0.set_channel_map(([self.channel_number]))


def main(top_block_cls=rcv_single_fm, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
