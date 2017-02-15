#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Receive Single FM Station
# Author: Nathan West
# Generated: Wed Feb 15 15:02:22 2017
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


class rcv_single_fm_channelize_channel_power(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "rcv_single_fm_channelize_channel_power")
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
        self.pfb_channelizer_ccf_0 = pfb.channelizer_ccf(
        	  100,
        	  (fm_taps),
        	  1.0,
        	  100)
        self.pfb_channelizer_ccf_0.declare_sample_delay(0)

        self.channel_power_display = qtgui.vector_sink_f(
            100,
            0,
            1.0,
            "x-Axis",
            "y-Axis",
            "Power per FM Channel",
            1 # Number of inputs
        )
        self.channel_power_display.set_update_time(0.10)
        self.channel_power_display.set_y_axis(-140, 10)
        self.channel_power_display.enable_autoscale(False)
        self.channel_power_display.enable_grid(False)
        self.channel_power_display.set_x_axis_units("")
        self.channel_power_display.set_y_axis_units("")
        self.channel_power_display.set_ref_level(0)

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
                self.channel_power_display.set_line_label(i, "Data {0}".format(i))
            else:
                self.channel_power_display.set_line_label(i, labels[i])
            self.channel_power_display.set_line_width(i, widths[i])
            self.channel_power_display.set_line_color(i, colors[i])
            self.channel_power_display.set_line_alpha(i, alphas[i])

        self._channel_power_display_win = sip.wrapinstance(self.channel_power_display.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._channel_power_display_win)
        self.blocks_streams_to_vector_0 = blocks.streams_to_vector(gr.sizeof_float*1, 100)

        ##################################################
        # Connections
        ##################################################
        for channel_number in range(100):
            resampler = filter.rational_resampler_ccc(
                interpolation=fm_channel_rate,
                decimation=int(200e3),
                taps=None,
                fractional_bw=None)
            mag_squarer = blocks.complex_to_mag_squared(1)
            dber = blocks.nlog10_ff(10.)
            self.connect((self.pfb_channelizer_ccf_0, channel_number), (resampler, 0))
            self.connect((resampler, 0), (mag_squarer, 0))
            self.connect((mag_squarer, 0), (dber, 0))
            self.connect((dber, 0), (self.blocks_streams_to_vector_0, channel_number))


        self.connect((self.blocks_streams_to_vector_0, 0), (self.channel_power_display, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.pfb_channelizer_ccf_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_waterfall_sink_x_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "rcv_single_fm_channelize_channel_power")
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

    def get_fm_channel_rate(self):
        return self.fm_channel_rate

    def set_fm_channel_rate(self, fm_channel_rate):
        self.fm_channel_rate = fm_channel_rate

    def get_channel_number(self):
        return self.channel_number

    def set_channel_number(self, channel_number):
        self.channel_number = channel_number
        self.pfb_channelizer_ccf_0.set_channel_map(([self.channel_number]))


def main(top_block_cls=rcv_single_fm_channelize_channel_power, options=None):

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
