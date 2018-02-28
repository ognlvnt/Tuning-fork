#!/usr/bin/env Python
#A note for tuning guitar
#02.02.2018


from gnuradio import analog
from gnuradio import gr
from gnuradio import eng_notation
from gnuradio import audio


class top_block(gr.top_block):
	def __init__(self):
		gr.top_block.__init__(self)

		sample_rate = 32000
		amp = 0.1

		source = analog.sig_source_f(sample_rate, analog.GR_SIN_WAVE,440,amp)
		sink = audio.sink(sample_rate,"")

		self.connect(source,(sink,0))

if __name__=='__main__':
	try:
		top_block().run()
	except[[KeyboardInterrupt]]:
		pass
