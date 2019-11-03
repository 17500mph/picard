$noop(★ For Development Only - Variable Settings in Subsections ★)
$noop(★ Where Available - Audio Metrics Only at this Time ★)
$set(_devMode,1)
$noop(####################### Scratch Space ######################)
$if($eq(,),)
$set(%comment%,%_originalFileName% []%comment%)
$noop(####################### END SETTINGS #######################)

$noop(########### Audio Metrics Setup  ###########################)
$noop(########### DevMode Values Only ############################)
$set(_biitrate,192)
$set(_saample,44100)
$set(_biits_per_sample,16)
$set(_chaannels,2)
$set(_tiitle,My Great Score)
$noop(########### CONFIRM DevMode is Disabled for Live Use ########)

$if($eq(%_devMode%,1)$set(_bitRateSpeed,%_sample%KHz ),$set(_bitRateSpeed,%_saample%KHz ))
$if($eq(%_devMode%,1)$set(_bitRateValue,$left(,3)%_bitrate%),$set(_bitRateValue,$left(,3)%_biitrate%))
$if($eq(%_devMode%,1)$set(_bitRateValue,$left(,3)%_bitrate%),$set(_bitRateValue,$left(,3)%_biitrate%))
$if($eq(%_devMode%,1)$set(_bitsPerSample,[%_bits_per_sample%]bit),$set(_bitsPerSample,[%_biits_per_sample%]bit))
$if($eq(%_devMode%,1)$set(_audioChannels,%_channels%ch]),$set(_audioChannels,%_chaannels%ch]))
$if($eq(%_devMode%,1),)$set(_titleForFilename,%_tiitle%)

$set(_bitRateType,$if($eq_any(%_bitRateValue%,320,256,224,192,160,128,112,96,80,64,56,48,40,32,24,16,8),CBR$set(_cbrRateValue,%_bitRateValue%),VBR$set(_vbrRateValue,%_bitRateValue%)))

$noop(Bitrate factors of 8.0 are most likely CBR with the remainder being VBR)

$if($eq(%_cbrRateValue%,320),$set(_fileCBRRate,[320 ),
$if($eq(%_cbrRateValue%,256),$set(_fileCBRRate,[256 ),
$if($eq(%_cbrRateValue%,224),$set(_fileCBRRate,[224 ),
$if($eq(%_cbrRateValue%,192),$set(_fileCBRRate,[192 ),
$if($eq(%_cbrRateValue%,160),$set(_fileCBRRate,[160 ),
$if($eq(%_cbrRateValue%,128),$set(_fileCBRRate,[128 ),
$if($eq(%_cbrRateValue%,112),$set(_fileCBRRate,[112 ),
$if($eq(%_cbrRateValue%,96),$set(_fileCBRRate,[96 ),
$if($eq(%_cbrRateValue%,80),$set(_fileCBRRate,[80 ),
$if($eq(%_cbrRateValue%,64),$set(_fileCBRRate,[64 ),
$if($eq(%_cbrRateValue%,56),$set(_fileCBRRate,[56 ),
$if($eq(%_cbrRateValue%,48),$set(_fileCBRRate,[48 ),
$if($eq(%_cbrRateValue%,40),$set(_fileCBRRate,[40 ),
$if($eq(%_cbrRateValue%,32),$set(_fileCBRRate,[32 ),
$if($eq(%_cbrRateValue%,24),$set(_fileCBRRate,[24 ),
$if($eq(%_cbrRateValue%,16),$set(_fileCBRRate,[16 ),
$if($eq(%_cbrRateValue%,8),$set(_fileCBRRate,[8 ),
										      ))))))))))))))))))

$if($eq(%_bitRateType%,VBR),
$if($gt(%_vbrRateValue%,319),$set(_fileVBRRate,[320+ ),
$if($gt(%_vbrRateValue%,220),$set(_fileVBRRate,[V0 ),
$if($gt(%_vbrRateValue%,191),$set(_fileVBRRate,[V1 ),
$if($gt(%_vbrRateValue%,170),$set(_fileVBRRate,[V2 ),
$if($gt(%_vbrRateValue%,150),$set(_fileVBRRate,[V3 ),
$if($gt(%_vbrRateValue%,140),$set(_fileVBRRate,[V4 ),
$if($gt(%_vbrRateValue%,130),$set(_fileVBRRate,[V5 ),
$if($gt(%_vbrRateValue%,120),$set(_fileVBRRate,[V6 ),
												)))))))))

$noop(######### File Naming Structure Variables Complete #########)


$noop(★ GAME OVER ★)
%_titleForFilename%

$if($eq(%_showTime%,1), [%_length%] )
$if($eq(%_showBandwidth%,1)%_bitRateType%,)%_fileCBRRate%%_fileVBRRate%%_bitRateSpeed%%_bitRateType% %_audioChannels%)

$noop(★ 00 CREDITS ★)