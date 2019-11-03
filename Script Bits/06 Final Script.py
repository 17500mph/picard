$noop(★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★)
$noop(★ MBP YA Magic-Script that does more stuff too. - v2.1a - amd/17500mph ★)
$noop(★                                                                      ★)
$noop(★ Here is a script for music renaming in MusicBrainz Picard            ★)
$noop(★                                                                      ★)
$noop(★ Features :                                                           ★)
$noop(★                                                                      ★)
$noop(★   Individualy Selectable Root Directory Organization Options:        ★)
$noop(★                                                                      ★)
$noop(★ • Directories by [A]rtist Name / [N]ame, Artist or last.fm** category★)
$noop(★ • subDirectory for each main type [Album/Single/EP...]               ★)
$noop(★ • Separate Root directory for compilations [!various]                ★)
$noop(★ • Single Artist Compilations go in Artist Directory                  ★)
$noop(★ • Root directory Audio Books, Podcasts, Others                       ★)
$noop(★                                                                      ★)
$noop(★  ~/MusicRoot/[O]/Oingo Boingo/[Artist Compilations]/                 ★)
$noop(★  ~/MusicRoot/Compilations/K-Tel Hits of the 1980s Vol. 1             ★)
$noop(★  ~/MusicRoot/Audio Books/Ready Player One                            ★)
$noop(★  ~/MusicRoot/Podcasts/Mad Mad Music #29                              ★)
$noop(★                                                                      ★)
$noop(★ - Alphabetize artist without leading "The"                           ★)
$noop(★ - Show Album Release Status on Album Directory                       ★)
$noop(★ - Show Record Label on Directory Name Directory                      ★)
$noop(★ - Show Catalogue Number in Album Directory Name                      ★)
$noop(★ - Show Track Duration in Filename                                    ★)
$noop(★ - Filtered character for files & directory naming                    ★)
$noop(★ - Include media type in directory name [when its not CD]             ★)
$noop(★ - Multi-Disc SubDirectory per Disc in Album Directory                ★)
$noop(★ - Custom directory tag for multi-disc CD/Vinyl [CD1/Disc1 by default]★)
$noop(★ - Put multi-CD release in same directory [names become 101/102/201..]★)
$noop(★ - Vinyl can use musicbrainz style for track [A1/A2/B1...]            ★)
$noop(★ - File Type SubDirectory in Album Directory                          ★)
$noop(★                                                                      ★)
$noop(★ ** Optional Plugin Needed for Last.fm [for category trending]        ★)
$noop(★   -> https://github.com/fdemmer/Picard-Last.fm.ng-Plugin             ★)
$noop(★                                                                      ★)
$noop(★ - DevMode:                                                           ★)
$noop(★   Allows better simulation control of variables for debugging        ★)
$noop(★                                                                      ★)
$noop(★ Do Not Taunt The Happy Tagging Ball                                  ★)
$noop(★                                                                      ★)
$noop(★----------------------------------------------------------------------★)
$noop(★   Based on the MBP Magic Script  By Ski-lleR                         ★)
$noop(★   Thanks to avibrazil for his filter                                 ★)
$noop(★ > https://github.com/avibrazil/picard-scripting                      ★)
$noop(★----------------------------------------------------------------------★)
$noop(★                                                                      ★)
$noop(★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★)
$noop(★ INSERT COIN ★)

$noop(Configuration Section - 0-Disable / 1-Enable)

$noop(★ GLOBAL ★)

$noop(★ Sort orderTypeForRoot ★)
$noop(★ ~/Music/Last.fm Genre/A/Artist/AlbumTitle/ ★)
$noop(★  1: Category [Last.fm.ng] ★)
$noop(★ ~/Music/A/Artist/AlbumTitle/ ★)
$noop(★  2: Artist first letter ★)
$set(_orderTypeForRoot,2)


$noop(★ Sort orderTypeForArtist ★)
$noop(★  1: First letter of first name ★)
$noop(★ ~/Music/M/Music Artist/AlbumTitle/  ★)
$noop(★  2: First letter of last name ★)
$noop(★ ~/Music/A/Artist, Music/AlbumTitle/  ★)
$set(_orderTypeForArtist,2)

$noop(★ How to designate Complete Albums that contain multiples of at least 1 Track 1 ★)
$noop(★ 0, They are Handled as InComplete ★)
$noop(★ 1  They are Handled as Complete w/starred but not Gold icon★)
$set(_extraTrackHandling,1)


$noop(★ 1  Earlier in the Sort Artist Diversion?★)
$set(_earlierLevelArtistSeparation,0)
$noop(★ 0  Earlier in the Sort Incomplete Diversion?★)
$set(_earlierPresortForIncompletes,1)

$noop(★ Do you want separation by type / extension at the Root Level? ★)
$noop(★ ~/Music/MP3/AlbumTitle/ - ~/Music/FLAC/AlbumTitle/ - ~/Music/M4A/AlbumTitle/ - ~/Music/WNA/AlbumTitle/ ★)
$set(_rootLevelTypeSeparation,0)

$noop(★ Do you want separatation by type / extension at the Album Level? ★)
$noop(★ ~/Music/AlbumTitle/MP3/ - ~/Music/AlbumTitle/FLAC/ - ~/Music/AlbumTitle/M4A - ~/Music/AlbumTitle/WNA/ ★)
$set(_albumLevelTypeSeparation,1)

$noop(★ Do you want the Album Title added before the type / extension after the Album Level? ★)
$noop(★ ~/Music/AlbumTitle/AlbumTitle MP3/ - ~/Music/AlbumTitle/AlbumTitle FLAC/ - ~/Music/AlbumTitleAlbumTitle /M4A ★)
$set(_albumNameAtTypeSeparation,1)

$noop(Album Name/EP/Single/Live/Album etc.)
$noop(★ ~/Music/AlbumTitle/AlbumTitle MP3/Single/ - ~/Music/AlbumTitle/AlbumTitle FLAC/EP/ ★)
$set(_separateByTypeInArtistDirectory,1)

$noop(★ Do you want Tribute and Cover Albums Placed with Artist being attributed? ★)
$noop(★ ~/Music/AlbumTitle/AlbumTitle MP3/Cover/ - ~/Music/AlbumTitle/AlbumTitle FLAC/Tribute/ ★)
$noop(★ Requires Custom Use of AlbumArtistSort and ArtistSort Tags ★)
$noop(Enter “Tribute” or “Cover” in the Album Sort as field.)
$noop(Enter the Artist in the Album Artist Sort as field.)
$set(_altArtistSort,1/)

$set(_separateAlbum,0) $noop(Albums in SubDirectory as well)
$noop(★ ~/Music/A/Artist, Music/Album/AlbumTitle ★)

$set(_compilationsGSubDirectory,Compilations/)
$noop(★ ~/Music/Compilations/  ★)

$noop(★ SOUNDTRACK/VARIOUS DIRECTORY ★)
$set(_soundTracksDirectory,Soundtrack/)
$set(_variousArtistsDirectory,Various/)
$set(_audiobooksDirectory,Audiobook/)
$set(_incompleteDirectory,Partial)
$set(_podcastSubDirectory,Podcast/)

$noop(★ Multi-Disc ★)

$noop(★ ~/Music/A/Artist, Music/AlbumTitle/Disc01/01 - Tracklist ★)
$set(_useSubDiscDirectory,1)

$noop(★ ~/Music/A/Artist, Music/AlbumTitle/01 - Tracklist ***SKIP SubDiscDirectory if only one Medium in Realease ★)
$set(_mergeDiscWhenNotUsingSubDirectory,0)

$set(_showDiscSubtitle,1)
$set(_nameForTypeCD,Disc)
$set(_nameForTypeVinyl,Side)

$noop(★ ~/Music/A/Artist, Music/AlbumTitle/A1 ,A2 ,B1, B2 Tracklist - ★)
$set(_useMusicBrainzStyleForVinylTrack,1)

$noop(★ Custom Subdirectory Titles at Artist Level ★)
$noop(★ ~/Music/A/Artist, Music/EP/AlbumTitle ~/Music/A/Artist, Music/Live/AlbumTitle ★)


$set(_albumSubDirectory,Album/)
$set(_compilationsASubDirectory,Compilation/)
$set(_coverSubDirectory,[Cover]/)
$set(_tributeSubDirectory,[Tribute]/)
$set(_singlesSubDirectory,[Single]/)
$set(_liveSubDirectory,[Live]/)
$set(_epSubDirectory,[EP]/)
$set(_broadcastSubDirectory,[Broadcast]/)
$set(_videoSubDirectory,[Video]/)
$set(_otherSubDirectory,[Others]/)
$set(_extDirectory,%_extension%/)

$noop(★ Other Values Included in Filename ★)
$set(_showRecordLabel,1)
$set(_showTime,1)
$set(_showDate,1)
$set(_showReleaseStatus,1)
$set(_showBandwidth,1)
$set(_showCatalogueNumber,1)

$noop(★ For Development Only - Variable Settings in Subsections ★)
$noop(★ Where Available - Audio Metrics Only at this Time ★)
$set(_devMode,0)
$noop(####################### Scratch Space ######################)
$noop( )
$noop(####################### END SETTINGS #######################)

$noop(★ Unless you're changing appearances, there isn't really anything to do past here ★)

$noop(########## DETECT MUSIC TYPE ###############################)

$noop(★ Detect Album ★)
$if($in(%releasetype%,album),
  $set(_isAlbum,1)
)
$noop(★ Detect Single ★)
$if($in(%releasetype%,single),
  $set(_isSingle,1)
)
$noop(★ Detect Live ★)
$if($in(%releasetype%,live),
  $set(_isLive,1)
)
$noop(★ Detect EP ★)
$if($in(%releasetype%,ep),
  $set(_isEP,1)
)
$noop(★ Detect Broadcast ★)
$if($in(%releasetype%,broadcast),
  $set(_isBroadcast,1)
)
$noop(★ Detect Artist Compilation ★)
$if($in(%releasetype%,compilation),
  $set(_isArtistCompil,1)
)
$noop(★ Detect Audiobook ★)
$if($in(%releasetype%,audiobook),  $set(_isAudiobook,1)
)
$noop(★ Detect Other ★)
$if($in(%releasetype%,other),
  $set(_isOther,1)
)
$noop(★ Detect Tribute ★)
$if($in(%albumsort%,Tribute),
  $set(_isTribute,1)
)
$noop(★ Detect Cover ★)
$if($in(%albumsort%,Cover),
  $set(_isCover,1)
)
$noop(★ Detect Podcast ★)
$if($in(%genre%,Podcast),
  $set(_isPodcast,1)
)
$noop(★ Detect Soundtrack ★)
$if($in(%releasetype%,soundtrack),
  $set(_isSoundTrack,1)
)
$noop(★ Detect Incomplete ★)
$if($eq($is_complete(),0),
  $set(_isIncomplete,1)
)
$noop(★ Detect Video ★)
$if($eq($is_video(),0),
  $set(_isVideo,1)
)
$noop(★ Detect Various Artist ★)
$if($eq(%albumartist%,Various Artists),
  $set(_isVarious,1)
)
$noop(★ Re-detect Compilation Type ★)
$if($eq(%compilation%,1),
  $set(_isGlobalCompil,1)
)
$noop(★ Detect Global Compilation ★)
$if($eq(%_isGlobalCompil%,1), $set(_isArtistCompil,0)
)

$noop(★ Get Track Length ★)
$if($eq(%_showTime%,1),
$noop($set(_trackLength,%length%))
)
$noop(########## Start TAG Manipulation ##########################)
$noop(★ Organize artist by alphabetical Directories excluding leading The ★)
$set(albumartist,$if($eq($left(%albumartist%,4),The ),%albumartistsort%,%albumartist%))
$set(_originalFileName,%_filename%)

$noop(########## Start TAG Formatting  ###########################)
$noop(★ Typography for tags: changes will affect tags on media ★)

$noop(★ ... ➡ …)
$set(album,$replace(%album%,...,…))
$set(title,$replace(%title%,...,…))
$set(discsubtitle,$replace(%discsubtitle%,...,…))

$noop(★ No. ➡ №)
$set(album,$replace(%album%, [Nn]o.\\s*\(\\d\), №\\1))
$set(title,$rreplace(%title%, [Nn]o.\\s*\(\\d\), №\\1))
$set(discsubtitle,$replace(%discsubtitle%, [Nn]o.\\s*\(\\d\), №\\1))

$noop(★ [digit]" ➡ [digit]″)
$set(discsubtitle,$rreplace(%discsubtitle%,\(\\d\)",\\1''))

$noop(★ "12" Vinyl" ➡ "12 Inch Vinyl")
$set(media,$rreplace(%media%,\(\\d\)",\\ Inch))
$set(album,$rreplace(%album%,\(\\d\)",\\ Inch))
$set(title,$rreplace(%title%,\(\\d\)",\\ Inch))

$noop(★ "something" ➡ “something” single quote for server/samba)
$set(albumartist,$rreplace(%albumartist%,"\(.*?\)",'\\1'))
$set(artist,$rreplace(%artist%,"\(.*?\)",'\\1'))
$set(albumartistsort,$rreplace(%albumartistsort%,"\(.*?\)",'\\1'))
$set(artistsort,$rreplace(%artistsort%,"\(.*?\)",'\\1'))
$set(album,$rreplace(%album%,"\(.*?\)",'\\1'))
$set(title,$rreplace(%title%,"\(.*?\)",'\\1'))
$set(discsubtitle,$rreplace(%discsubtitle%,"\(.*?\)",'\\1'))

$noop(########## Start File Naming Structure Variables ###########)

$noop(★ Typography on file naming only ★)
$set(_titleForFilename,%title%)
$set(_albumForFilename,%album%)
$set(_discsubtitleForFilename,%discsubtitle%)
$set(_albumartistForFilename,%albumartist%)
$set(_artistForFilename,%artist%)
$set(_albumartistsortForFilename,%albumartistsort%)
$set(_artistsortForFilename,%artistsort%)

$noop(★ # ➡ ♯)
$set(_titleForFilename,$replace(%_titleForFilename%,#,♯))
$set(_albumForFilename,$replace(%_albumForFilename%,#,♯))
$set(_discsubtitleForFilename,$replace(%_discsubtitleForFilename%,#,♯))

$noop(★ ;: ➡ h, m,)
$set(_trackLength,$replace(%_trackLength%,:,m))

$noop(★ : ➡ ∶)
$set(_titleForFilename,$replace(%_titleForFilename%,:,∶))
$set(_albumForFilename,$replace(%_albumForFilename%,:,∶))
$set(_discsubtitleForFilename,$replace(%_discsubtitleForFilename%,:,∶))
$set(_artistForFilename,$replace(%_artistForFilename%,:,∶))
$set(_albumartistForFilename,$replace(%_albumartistForFilename%,:,∶))
$set(_artistsortForFilename,$replace(%_artistsortForFilename%,:,∶))
$set(_albumartistsortForFilename,$replace(%_albumartistsortForFilename%,:,∶))

$noop(★ ? ➡ ⁇)
$set(_titleForFilename,$replace(%_titleForFilename%,?,⁇))
$set(_albumForFilename,$replace(%_albumForFilename%,?,⁇))
$set(_discsubtitleForFilename,$replace(%_discsubtitleForFilename%,?,⁇))
$set(_artistForFilename,$replace(%_artistForFilename%,?,⁇))
$set(_artistsortForFilename,$replace(%_artistsortForFilename%,?,⁇))

$set(_titleForFilename,$replace(%_titleForFilename%,|,￨))
$set(_albumForFilename,$replace(%_albumForFilename%,|,￨))
$set(_discsubtitleForFilename,$replace(%_discsubtitleForFilename%,|,￨))

$set(_titleForFilename,$replace(%_titleForFilename%,>,＞))
$set(_albumForFilename,$replace(%_albumForFilename%,>,＞))
$set(_discsubtitleForFilename,$replace(%_discsubtitleForFilename%,>,＞))

$set(_titleForFilename,$replace(%_titleForFilename%,<,＜))
$set(_albumForFilename,$replace(%_albumForFilename%,<,＜))
$set(_discsubtitleForFilename,$replace(%_discsubtitleForFilename%,<,＜))

$set(_titleForFilename,$replace(%_titleForFilename%,*,✱))
$set(_albumForFilename,$replace(%_albumForFilename%,*,✱))
$set(_discsubtitleForFilename,$replace(%_discsubtitleForFilename%,*,✱))
$set(_artistForFilename,$replace(%_artistForFilename%,*,✱))
$set(_albumartistForFilename,$replace(%_albumartistForFilename%,*,✱))
$set(_artistsortForFilename,$replace(%_artistsortForFilename%,*,✱))
$set(_albumartistsortForFilename,$replace(%_albumartistsortForFilename%,*,✱))

$set(_titleForFilename,$replace(%_titleForFilename%,&,＆))
$set(_albumForFilename,$replace(%_albumForFilename%,&,＆))
$set(_discsubtitleForFilename,$replace(%_discsubtitleForFilename%,&,＆))
$set(_artistForFilename,$replace(%_artistForFilename%,&,＆))
$set(_albumartistForFilename,$replace(%_albumartistForFilename%,&,＆))
$set(_artistsortForFilename,$replace(%_artistsortForFilename%,&,＆))
$set(_albumartistsortForFilename,$replace(%_albumartistsortForFilename%,&,＆))
$noop(★ For Development Only - Variable Settings in Subsections ★)
$noop(★ Where Available - Audio Metrics Only at this Time ★)

$noop(########### Audio Metrics Setup  ###########################)
$noop(########### DevMode Values Only ############################)

$set(_devMode,0) $noop(This one is here for convenience, for now this works here, too. But it will need to go later.)

$set(_biitrate,192)
$set(_saample_rate,44100)
$set(_biits_per_sample,16)
$set(_chaannels,2)
$set(_tiitle,My Great Score)
$noop(########### CONFIRM DevMode is Disabled for Live Use ########)
$noop({%title% - %_bitrate% - %_sample_rate% - %_bits_per_sample% - %_channels%})

$if($eq(%_devMode%,1),$set(_bitRateValue,$left(%_biitrate%,3)),$set(_bitRateValue,$left(%_bitrate%,3)))
$if($eq(%_devMode%,1),$set(_bitRateSpeed,%_saample_rate%KHz),$set(_bitRateSpeed,%_sample_rate%KHz ))
$if($eq(%_devMode%,1),$set(_bitsPerSample,[%_biits_per_sample%]bit),$set(_bitsPerSample,[%_bits_per_sample%]bit ))
$if($eq(%_devMode%,1),$set(_audioChannels,%_chaannels%ch]),$set(_audioChannels,%_channels%ch]))
$if($eq(%_devMode%,1),$set(_titleForFilename,%title%),$set(_titleForFilename,%title%))

$noop({%title% - %_bitRateValue% - %_bitRateSpeed% - %_bitsPerSample% - %_audioChannels% - %_titleForFilename% - %_fileCBRRate% - %_fileVBRRate% -  %_bitrate% - %_biitrate%})

$noop(Bitrate factors of 8.0 are CBR, Anything else is VBR)

$set(_bitRateType,$if($eq_any(%_bitRateValue%,320,256,224,192,160,128,112,96,80,64,56,48,40,32,24,16,8),CBR $set(_cbrRateValue,%_bitRateValue%),VBR $set(_vbrRateValue,%_bitRateValue%)))

$noop(Bitrate factors of 8.0 are most likely CBR with the remainder being VBR)

$if($eq(%_cbrRateValue%,320),$set(_fileCBRRate,320 ),
$if($eq(%_cbrRateValue%,256),$set(_fileCBRRate,256 ),
$if($eq(%_cbrRateValue%,224),$set(_fileCBRRate,224 ),
$if($eq(%_cbrRateValue%,192),$set(_fileCBRRate,192 ),
$if($eq(%_cbrRateValue%,160),$set(_fileCBRRate,160 ),
$if($eq(%_cbrRateValue%,128),$set(_fileCBRRate,128 ),
$if($eq(%_cbrRateValue%,112),$set(_fileCBRRate,112 ),
$if($eq(%_cbrRateValue%,96),$set(_fileCBRRate,96 ),
$if($eq(%_cbrRateValue%,80),$set(_fileCBRRate,80 ),
$if($eq(%_cbrRateValue%,64),$set(_fileCBRRate,64 ),
$if($eq(%_cbrRateValue%,56),$set(_fileCBRRate,56 ),
$if($eq(%_cbrRateValue%,48),$set(_fileCBRRate,48 ),
$if($eq(%_cbrRateValue%,40),$set(_fileCBRRate,40 ),
$if($eq(%_cbrRateValue%,32),$set(_fileCBRRate,32 ),
$if($eq(%_cbrRateValue%,24),$set(_fileCBRRate,24 ),
$if($eq(%_cbrRateValue%,16),$set(_fileCBRRate,16 ),
$if($eq(%_cbrRateValue%,8),$set(_fileCBRRate,8 ),
										      )))))))))))))))))

$if($eq(%_bitRateType%,VBR)$set(_fileVBRRate,%_vbrRateValue% ) ,
$if($gt(%_vbrRateValue%,319),$set(_fileVBRRate,320+ ),
$if($gt(%_vbrRateValue%,220),$set(_fileVBRRate,V0 ),
$if($gt(%_vbrRateValue%,191),$set(_fileVBRRate,V1 ),
$if($gt(%_vbrRateValue%,170),$set(_fileVBRRate,V2 ),
$if($gt(%_vbrRateValue%,150),$set(_fileVBRRate,V3 ),
$if($gt(%_vbrRateValue%,140),$set(_fileVBRRate,V4 ),
$if($gt(%_vbrRateValue%,130),$set(_fileVBRRate,V5 ),
$if($gt(%_vbrRateValue%,120),$set(_fileVBRRate,V6 ),
												)))))))))
$noop(######### File Naming Structure Variables Complete #########)



$noop(★ Pathname Generation Starts Here ★)

$noop(★ Root level Path ★)
$noop(   root = '/Volumes/Drive/Music/ ... [Destination Directory Setting])


$noop(★ Separate by Format at root directory ★)
$noop(   rootLevelPath/MP3/Artist/Album ...)
$if($eq(%_rootLevelTypeSeparation%,1),$upper(%_extension%),)

$noop(   Earlier Incomplete Separation for Sorting ...)
$if($eq(%_earlierPresortForIncompletes%,1),$if($eq($is_complete(),0),$if($lt($matchedtracks(),%_totalalbumtracks%),# - %_incompleteDirectory%)),$if(%_isIncomplete%,# - %_incompleteDirectory%,))/
$if($eq(%_earlierLevelArtistSeparation%,1),%_artistForFilename%/)

$noop(★ Soundtrack in custom directory ,after soundtracksDirectory?? ★)
$noop(   root/*/Audio Books/Title ...)
$noop(   root/*/Soundtracks/Title ...)
$noop(   root/*/Podcasts/Title ...)
$if(%_isSoundTrack%,%_soundTracksDirectory%$left($swapprefix(%album%,A,An,The),1)/,/
$if(%_isAudiobook%,%_audiobooksDirectory%$left($swapprefix(%album%,A,An,The),1)/,/)
$if(%_isPodcast%,%_podcastDirectory%$left($swapprefix(%album%,A,An,The),1)/,/)

$noop(★ Various in custom directory ★)
$noop(root/<*>/Various)
$if(%_isVarious%,%_variousArtistsDirectory%$left($swapprefix(%album%,A,An,The),1)/,/
	$if(%_isGlobalCompil%,%_compilationsGSubDirectory%$left($swapprefix(%album%,A,An,The),1)/,/)
	$noop(★ Order root by category ★)
	$if($eq(%_orderTypeForRoot%,1),
	$if2(%albumgrouping%,Unknown)
	)/

$noop(★ Order root by artist ★)
$noop(root/<*>/<Last.FM=>/)
$noop(root/<*>/D/)
$if($eq(%_orderTypeForRoot%,2),
	$if($eq(%_orderTypeForArtist%,1),
		$upper($firstalphachar($if2(%_albumartistForFilename%, %_artistForFilename%),#)),
	$if($eq(%_orderTypeForArtist%,2),
		$if(%_isGlobalCompil%,,$upper($firstalphachar($if2(%_albumartistsortForFilename%, %_artistsortForFilename%),#)))
	))
)/

$noop(★ Artist with first letter of first name ★)
$noop(root/<*>/B/The B-52's)
$if($eq(%_orderTypeForArtist%,1),
$if2(%_artistSort%,%_albumartistForFilename%,%_artistForFilename%)
)/

$noop(★ Artist with first letter of last name ★)
$noop(root/<*>/B/B-52's, The)
$if($eq(%_orderTypeForArtist%,2),
$if(%_isGlobalCompil%,,$if2(%_albumartistsortForFilename%,%_artistsortForFilename%))
)/


$noop(★ Using Alternate Artists Directory For Covers & Tributes  **Uses Order for Album Artist tag [Field]★)

	$noop(root/<*>/O/Oingo Boingo/[Tributes]/DeadBandsParty)
	$if($eq_all(%_orderTypeForArtist%,%_isTribute%,1),
	$if2(%_artistSort%,%_albumartistForFilename%,%_artistForFilename%)
	)/

	$noop(root/<*>/D/DEVO/[Covers]/Devolution)
	$if($eq_all(%_orderTypeForArtist%,%_isCover%,1),
	$if2(%_artistSort%,%_albumartistForFilename%,%_artistForFilename%)
	)/
	$noop(★ Organize by type ★)
	$noop(root/<*>/Y/Yes/[Live]/90125 Live)
	$noop(root/<*>/Y/Yes,/90125)
	$if($eq(%_separateByTypeInArtistDirectory%,1),
		$if($eq(%_isArtistCompil%,1),%_compilationsASubDirectory%,
			$if($eq(%_isLive%,1),%_liveSubDirectory%,
				$if($eq(%_isCover%,1),%_coverSubDirectory%,
					$if($eq(%_isTribute%,1),%_tributeSubDirectory%,
						$if($eq(%_isEP%,1),%_epSubDirectory%,
							$if($eq(%_isSingle%,1),%_singlesSubDirectory%,
								$if($eq(%_isBroadcast%,1),%_broadcastSubDirectory%,
									$if($eq(%_isVideo%,1),%_videoSubDirectory%,
										$if($eq(%_isOther%,1),%_otherSubDirectory%,
											$if($eq(%_isAlbum%,1),
											$if($eq(%_separateAlbum%,1),%_albumSubDirectory%))

											))))))))))))

$noop(root/<*>/B/B-52's, The]/Bouncing off the Satellites/ )
%_albumForFilename%
$noop(★ Bouncing off the Satellites [Media-Type]/ ★)
$noop($if($ne(%media%,CD),$if(%media%,[$rreplace(%media%,["″], Inch)])))
$if(%media%, [$title(%media%]),)

$noop($if($and(%media%,$ne(%media%,CD)),$if($in(%media%,Vinyl),$title( [%media%])),$upper( [%media%])))

$noop(★ Bouncing off the Satellites [Vinyl] [YEAR]/ ★)
$if($eq(%_showDate%,1),$if($if2(%date%,%originalyear%,%originaldate%), [$left($if2(%date%,%originalyear%,%originaldate%),4)], [0000]))
$noop(★ Bouncing off the Satellites [Vinyl] [1986] [Release Status]/ ★)
$if(%releasestatus%,$if($eq(%_showReleaseStatus%,1),$title( [%releasestatus%])))

$noop(★ Bouncing off the Satellites [Vinyl] [1986] [Official] [Label]/ ★)
$if(%label%,$if(%_showRecordLabel%, $if(%label%,$title([%label%]))))

$noop(★ Bouncing off the Satellites [Vinyl] [1986] [Official] [MCA] [CAT-Number]/ ★)
$if(%catalognumber%,$if($eq(%_showCatalogueNumber%,1),$title( [%catalognumber%])))

$noop(★ Bouncing off the Satellites [Vinyl] [1986] [Official] [MCA] [AB-DC001]/ ★)
$noop(★ Bouncing off the Satellites [Vinyl] [1986] [Official] [MCA] [AB-DC001] - Incomplete/ ★)
$if($eq(%_extraTrackHandling%,1),$if($eq($is_complete(),0),$if($lt($matchedtracks( ),%_totalalbumtracks%), - %_incompleteDirectory%)),$if(%_isIncomplete%, - %_incompleteDirectory%,))/

$noop(★ Bouncing off the Satellites [Vinyl] [1986] [Official] [MCA] [AB-DC001]/ MP3 / ★)
$noop(★ Bouncing off the Satellites [Vinyl] [1986] [Official] [MCA] [AB-DC001]/ Bouncing off the Satellites MP3 / ★)
$if($eq(%_albumLevelTypeSeparation%,1),$if($eq(%_albumNameAtTypeSeparation%,1),%_albumForFilename% ,)$upper(%_extension%))/

$noop(★ Bouncing off the Satellites [Vinyl] [1986] [Official] [MCA] [AB-DC001]/ .../ Disc # ★)
$if($gt(%totaldiscs%,1),$noop(
	)$if($lt(%totaldiscs%,10),$set(_discnumber, %discnumber%),$set(_discnumber,$num(%discnumber%,2)))$noop(
	)$if($in(%media%,Vinyl),$noop(
		)$set(_nameForDiscDirectory,@OSLASH@@OBRACKET@%_nameForTypeVinyl%%_discnumber%@CBRACKET@),$noop(
		)$set(_nameForDiscDirectory,@OSLASH@@OBRACKET@%_nameForTypeCD%%_discnumber%@CBRACKET@))$noop(
		)$if($and(%_discsubtitleForFilename%,$eq(%_showDiscSubtitle%,1)),$set(_nameForDiscDirectory,%_nameForDiscDirectory% - %_discsubtitleForFilename%))$noop(
		)$if($eq(%_useSubDiscDirectory%,1),$noop(
			)$set(_nameForDiscDirectory,$replace(%_nameForDiscDirectory%,@OSLASH@@OBRACKET@,/))$noop(
			)$set(_nameForDiscDirectory,$replace(%_nameForDiscDirectory%,@CBRACKET@,)),$noop(
			)$if($eq(%_mergeDiscWhenNotUsingSubDirectory%,1),$noop(
				)$unset(_nameForDiscDirectory),$noop(
				)$set(_nameForDiscDirectory,$replace(%_nameForDiscDirectory%,@OSLASH@@OBRACKET@,[))$noop(
			)$set(_nameForDiscDirectory,$replace(%_nameForDiscDirectory%,@CBRACKET@,]))$noop(
		))$noop(
	))$noop(
)$if(%_nameForDiscDirectory%,%_nameForDiscDirectory%))/

$noop(★ Track # Title --%_filebr% -- %bitrate% -- %BRType% -- %BrVBR% --  ★)
$if($in(%media%,Vinyl),$noop(
	)$if($eq(%_useMusicBrainzStyleForVinylTrack%,1),$noop(
		)$if(%_musicbrainz_tracknumber%,%_musicbrainz_tracknumber%. )$noop(
	)),$noop(
	)$if(%tracknumber%,$if($gt(%totaldiscs%,1),$if($and($eq(%_useSubDiscDirectory%,0),$eq(%_mergeDiscWhenNotUsingSubDirectory%,1)),%discnumber%))$num(%tracknumber%,2). ))

$noop(★ GAME OVER ★)
%_titleForFilename%
$if($eq(%_showTime%,1),[%_length%] )
$if($eq(%_showBandwidth%,1),[%_fileCBRRate%%_fileVBRRate%%_bitRateSpeed%%_bitRateType%%_audioChannels%])

$noop(★ 00 CREDITS ★)





Tweak for Album / Albun Artist Heirarchy



$noop(★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★)
$noop(★ MBP YA Magic-Script that does more stuff too. - v2.1b - amd/17500mph ★)
$noop(★                                                                      ★)
$noop(★ Here is a script for music renaming in MusicBrainz Picard            ★)
$noop(★                                                                      ★)
$noop(★ Features :                                                           ★)
$noop(★                                                                      ★)
$noop(★   Individualy Selectable Root Directory Organization Options:        ★)
$noop(★                                                                      ★)
$noop(★ • Directories by [A]rtist Name / [N]ame, Artist or last.fm** category★)
$noop(★ • subDirectory for each main type [Album/Single/EP...]               ★)
$noop(★ • Separate Root directory for compilations [!various]                ★)
$noop(★ • Single Artist Compilations go in Artist Directory                  ★)
$noop(★ • Root directory Audio Books, Podcasts, Others                       ★)
$noop(★                                                                      ★)
$noop(★  ~/MusicRoot/[O]/Oingo Boingo/[Artist Compilations]/                 ★)
$noop(★  ~/MusicRoot/Compilations/K-Tel Hits of the 1980s Vol. 1             ★)
$noop(★  ~/MusicRoot/Audio Books/Ready Player One                            ★)
$noop(★  ~/MusicRoot/Podcasts/Mad Mad Music #29                              ★)
$noop(★                                                                      ★)
$noop(★ - Alphabetize artist without leading "The"                           ★)
$noop(★ - Show Album Release Status on Album Directory                       ★)
$noop(★ - Show Record Label on Directory Name Directory                      ★)
$noop(★ - Show Catalogue Number in Album Directory Name                      ★)
$noop(★ - Show Track Duration in Filename                                    ★)
$noop(★ - Filtered character for files & directory naming                    ★)
$noop(★ - Include media type in directory name [when its not CD]             ★)
$noop(★ - Multi-Disc SubDirectory per Disc in Album Directory                ★)
$noop(★ - Custom directory tag for multi-disc CD/Vinyl [CD1/Disc1 by default]★)
$noop(★ - Put multi-CD release in same directory [names become 101/102/201..]★)
$noop(★ - Vinyl can use musicbrainz style for track [A1/A2/B1...]            ★)
$noop(★ - File Type SubDirectory in Album Directory                          ★)
$noop(★                                                                      ★)
$noop(★ ** Optional Plugin Needed for Last.fm [for category trending]        ★)
$noop(★   -> https://github.com/fdemmer/Picard-Last.fm.ng-Plugin             ★)
$noop(★                                                                      ★)
$noop(★ - DevMode:                                                           ★)
$noop(★   Allows better simulation control of variables for debugging        ★)
$noop(★                                                                      ★)
$noop(★ Do Not Taunt The Happy Tagging Ball                                  ★)
$noop(★                                                                      ★)
$noop(★----------------------------------------------------------------------★)
$noop(★   Based on the MBP Magic Script  By Ski-lleR                         ★)
$noop(★   Thanks to avibrazil for his filter                                 ★)
$noop(★ > https://github.com/avibrazil/picard-scripting                      ★)
$noop(★----------------------------------------------------------------------★)
$noop(★                                                                      ★)
$noop(★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★)
$noop(★ INSERT COIN ★)

$noop(Configuration Section - 0-Disable / 1-Enable)

$noop(★ GLOBAL ★)

$noop(★ Sort orderTypeForRoot ★)
$noop(★ ~/Music/Last.fm Genre/A/Artist/AlbumTitle/ ★)
$noop(★  1: Category [Last.fm.ng] ★)
$noop(★ ~/Music/A/Artist/AlbumTitle/ ★)
$noop(★  2: Artist first letter ★)
$set(_orderTypeForRoot,2)


$noop(★ Sort orderTypeForArtist ★)
$noop(★  1: First letter of first name ★)
$noop(★ ~/Music/M/Music Artist/AlbumTitle/  ★)
$noop(★  2: First letter of last name ★)
$noop(★ ~/Music/A/Artist, Music/AlbumTitle/  ★)
$set(_orderTypeForArtist,2)

$noop(★ How to designate Complete Albums that contain multiples of at least 1 Track 1 ★)
$noop(★ 0, They are Handled as InComplete ★)
$noop(★ 1  They are Handled as Complete w/starred but not Gold icon★)
$set(_extraTrackHandling,1)


$noop(★ 1  Earlier in the Sort Artist Diversion?★)
$set(_earlierLevelArtistSeparation,0)
$noop(★ 0  Earlier in the Sort Incomplete Diversion?★)
$set(_earlierPresortForIncompletes,1)

$noop(★ Do you want separation by type / extension at the Root Level? ★)
$noop(★ ~/Music/MP3/AlbumTitle/ - ~/Music/FLAC/AlbumTitle/ - ~/Music/M4A/AlbumTitle/ - ~/Music/WNA/AlbumTitle/ ★)
$set(_rootLevelTypeSeparation,0)

$noop(★ Do you want separatation by type / extension at the Album Level? ★)
$noop(★ ~/Music/AlbumTitle/MP3/ - ~/Music/AlbumTitle/FLAC/ - ~/Music/AlbumTitle/M4A - ~/Music/AlbumTitle/WNA/ ★)
$set(_albumLevelTypeSeparation,1)

$noop(★ Do you want the Album Title added before the type / extension after the Album Level? ★)
$noop(★ ~/Music/AlbumTitle/AlbumTitle MP3/ - ~/Music/AlbumTitle/AlbumTitle FLAC/ - ~/Music/AlbumTitleAlbumTitle /M4A ★)
$set(_albumNameAtTypeSeparation,1)

$noop(Album Name/EP/Single/Live/Album etc.)
$noop(★ ~/Music/AlbumTitle/AlbumTitle MP3/Single/ - ~/Music/AlbumTitle/AlbumTitle FLAC/EP/ ★)
$set(_separateByTypeInArtistDirectory,1)

$noop(★ Do you want Tribute and Cover Albums Placed with Artist being attributed? ★)
$noop(★ ~/Music/AlbumTitle/AlbumTitle MP3/Cover/ - ~/Music/AlbumTitle/AlbumTitle FLAC/Tribute/ ★)
$noop(★ Requires Custom Use of AlbumArtistSort and ArtistSort Tags ★)
$noop(Enter “Tribute” or “Cover” in the Album Sort as field.)
$noop(Enter the Artist in the Album Artist Sort as field.)
$set(_altArtistSort,1/)

$set(_separateAlbum,0) $noop(Albums in SubDirectory as well)
$noop(★ ~/Music/A/Artist/AlbumTitle, ~/Music/A/Artist/Albums/AlbumTitle ★)

$set(_showTrackArtistSeparation,0) $noop(Breakdown by Artist within Album ** Special Case Use / Usually Left Side Compilations)
$noop(★ ~/Music/A/Artist/AlbumTitle/Artist/Track, ~/Music/A/Artist/Albums/AlbumTitle/Artist/Track ★)



$set(_compilationsGSubDirectory,Compilations/)
$noop(★ ~/Music/Compilations/  ★)

$noop(★ SOUNDTRACK/VARIOUS DIRECTORY ★)
$set(_soundTracksDirectory,Soundtrack/)
$set(_variousArtistsDirectory,Various/)
$set(_audiobooksDirectory,Audiobook/)
$set(_incompleteDirectory,Partial)
$set(_podcastSubDirectory,Podcast/)

$noop(★ Multi-Disc ★)

$noop(★ ~/Music/A/Artist, Music/AlbumTitle/Disc01/01 - Tracklist ★)
$set(_useSubDiscDirectory,1)

$noop(★ ~/Music/A/Artist, Music/AlbumTitle/01 - Tracklist ***SKIP SubDiscDirectory if only one Medium in Realease ★)
$set(_mergeDiscWhenNotUsingSubDirectory,0)

$set(_showDiscSubtitle,1)
$set(_nameForTypeCD,Disc)
$set(_nameForTypeVinyl,Side)

$noop(★ ~/Music/A/Artist, Music/AlbumTitle/A1 ,A2 ,B1, B2 Tracklist - ★)
$set(_useMusicBrainzStyleForVinylTrack,1)

$noop(★ Custom Subdirectory Titles at Artist Level ★)
$noop(★ ~/Music/A/Artist, Music/EP/AlbumTitle ~/Music/A/Artist, Music/Live/AlbumTitle ★)


$set(_albumSubDirectory,Albums/)
$set(_compilationsASubDirectory,Compilation/)
$set(_coverSubDirectory,[Cover]/)
$set(_tributeSubDirectory,[Tribute]/)
$set(_singlesSubDirectory,[Single]/)
$set(_liveSubDirectory,[Live]/)
$set(_epSubDirectory,[EP]/)
$set(_broadcastSubDirectory,[Broadcast]/)
$set(_videoSubDirectory,[Video]/)
$set(_otherSubDirectory,[Others]/)
$set(_extDirectory,%_extension%/)

$noop(★ Other Values Included in Filename ★)
$set(_showRecordLabel,1)
$set(_showTime,1)
$set(_showDate,1)
$set(_showReleaseStatus,1)
$set(_showBandwidth,1)
$set(_showCatalogueNumber,1)

$noop(★ For Development Only - Variable Settings in Subsections ★)
$noop(★ Where Available - Audio Metrics Only at this Time ★)
$set(_devMode,0)
$noop(####################### Scratch Space ######################)
$noop( )
$noop(####################### END SETTINGS #######################)

$noop(★ Unless you're changing appearances, there isn't really anything to do past here ★)

$noop(########## DETECT MUSIC TYPE ###############################)

$noop(★ Detect Album ★)
$if($in(%releasetype%,album),
  $set(_isAlbum,1)
)
$noop(★ Detect Single ★)
$if($in(%releasetype%,single),
  $set(_isSingle,1)
)
$noop(★ Detect Live ★)
$if($in(%releasetype%,live),
  $set(_isLive,1)
)
$noop(★ Detect EP ★)
$if($in(%releasetype%,ep),
  $set(_isEP,1)
)
$noop(★ Detect Broadcast ★)
$if($in(%releasetype%,broadcast),
  $set(_isBroadcast,1)
)
$noop(★ Detect Artist Compilation ★)
$if($in(%releasetype%,compilation),
  $set(_isArtistCompil,1)
)
$noop(★ Detect Audiobook ★)
$if($in(%releasetype%,audiobook),  $set(_isAudiobook,1)
)
$noop(★ Detect Other ★)
$if($in(%releasetype%,other),
  $set(_isOther,1)
)
$noop(★ Detect Tribute ★)
$if($in(%albumsort%,Tribute),
  $set(_isTribute,1)
)
$noop(★ Detect Cover ★)
$if($in(%albumsort%,Cover),
  $set(_isCover,1)
)
$noop(★ Detect Podcast ★)
$if($in(%genre%,Podcast),
  $set(_isPodcast,1)
)
$noop(★ Detect Soundtrack ★)
$if($in(%releasetype%,soundtrack),
  $set(_isSoundTrack,1)
)
$noop(★ Detect Incomplete ★)
$if($eq($is_complete(),0),
  $set(_isIncomplete,1)
)
$noop(★ Detect Video ★)
$if($eq($is_video(),0),
  $set(_isVideo,1)
)
$noop(★ Detect Various Artist ★)
$if($eq(%albumartist%,Various Artists),
  $set(_isVarious,1)
)
$noop(★ Re-detect Compilation Type ★)
$if($eq(%compilation%,1),
  $set(_isGlobalCompil,1)
)
$noop(★ Detect Global Compilation ★)
$if($eq(%_isGlobalCompil%,1), $set(_isArtistCompil,0)
)

$noop(★ Get Track Length ★)
$if($eq(%_showTime%,1),
$noop($set(_trackLength,%length%))
)
$noop(########## Start TAG Manipulation ##########################)
$noop(★ Organize artist by alphabetical Directories excluding leading The ★)
$set(albumartist,$if($eq($left(%albumartist%,4),The ),%albumartistsort%,%albumartist%))
$set(_originalFileName,%_filename%)

$noop(########## Start TAG Formatting  ###########################)
$noop(★ Typography for tags: changes will affect tags on media ★)

$noop(★ ... ➡ …)
$set(album,$replace(%album%,...,…))
$set(title,$replace(%title%,...,…))
$set(discsubtitle,$replace(%discsubtitle%,...,…))

$noop(★ No. ➡ №)
$set(album,$replace(%album%, [Nn]o.\\s*\(\\d\), №\\1))
$set(title,$rreplace(%title%, [Nn]o.\\s*\(\\d\), №\\1))
$set(discsubtitle,$replace(%discsubtitle%, [Nn]o.\\s*\(\\d\), №\\1))

$noop(★ [digit]" ➡ [digit]″)
$set(discsubtitle,$rreplace(%discsubtitle%,\(\\d\)",\\1''))

$noop(★ "12" Vinyl" ➡ "12 Inch Vinyl")
$set(media,$rreplace(%media%,\(\\d\)",\\1 Inch))
$set(album,$rreplace(%album%,\(\\d\)",\\1 Inch))
$set(title,$rreplace(%title%,\(\\d\)",\\1 Inch))

$noop(★ "something" ➡ “something” single quote for server/samba)
$set(albumartist,$rreplace(%albumartist%,"\(.*?\)",'\\1'))
$set(artist,$rreplace(%artist%,"\(.*?\)",'\\1'))
$set(albumartistsort,$rreplace(%albumartistsort%,"\(.*?\)",'\\1'))
$set(artistsort,$rreplace(%artistsort%,"\(.*?\)",'\\1'))
$set(album,$rreplace(%album%,"\(.*?\)",'\\1'))
$set(title,$rreplace(%title%,"\(.*?\)",'\\1'))
$set(discsubtitle,$rreplace(%discsubtitle%,"\(.*?\)",'\\1'))

$noop(★ # ➡ ♯)
$set(_titleForFilename,$replace(%_titleForFilename%,#,♯))
$set(_albumForFilename,$replace(%_albumForFilename%,#,♯))
$set(_discsubtitleForFilename,$replace(%_discsubtitleForFilename%,#,♯))

$noop(★ ;: ➡ h, m,)
$set(_trackLength,$replace(%_trackLength%,:,m))

$noop(★ : ➡ ∶)
$set(_titleForFilename,$replace(%_titleForFilename%,:,∶))
$set(_albumForFilename,$replace(%_albumForFilename%,:,∶))
$set(_discsubtitleForFilename,$replace(%_discsubtitleForFilename%,:,∶))
$set(_artistForFilename,$replace(%_artistForFilename%,:,∶))
$set(_albumartistForFilename,$replace(%_albumartistForFilename%,:,∶))
$set(_artistsortForFilename,$replace(%_artistsortForFilename%,:,∶))
$set(_albumartistsortForFilename,$replace(%_albumartistsortForFilename%,:,∶))

$noop(★ ? ➡ ⁇)
$set(_titleForFilename,$replace(%_titleForFilename%,?,⁇))
$set(_albumForFilename,$replace(%_albumForFilename%,?,⁇))
$set(_discsubtitleForFilename,$replace(%_discsubtitleForFilename%,?,⁇))
$set(_artistForFilename,$replace(%_artistForFilename%,?,⁇))
$set(_artistsortForFilename,$replace(%_artistsortForFilename%,?,⁇))

$set(_titleForFilename,$replace(%_titleForFilename%,|,￨))
$set(_albumForFilename,$replace(%_albumForFilename%,|,￨))
$set(_discsubtitleForFilename,$replace(%_discsubtitleForFilename%,|,￨))

$set(_titleForFilename,$replace(%_titleForFilename%,>,＞))
$set(_albumForFilename,$replace(%_albumForFilename%,>,＞))
$set(_discsubtitleForFilename,$replace(%_discsubtitleForFilename%,>,＞))

$set(_titleForFilename,$replace(%_titleForFilename%,<,＜))
$set(_albumForFilename,$replace(%_albumForFilename%,<,＜))
$set(_discsubtitleForFilename,$replace(%_discsubtitleForFilename%,<,＜))

$set(_titleForFilename,$replace(%_titleForFilename%,*,✱))
$set(_albumForFilename,$replace(%_albumForFilename%,*,✱))
$set(_discsubtitleForFilename,$replace(%_discsubtitleForFilename%,*,✱))
$set(_artistForFilename,$replace(%_artistForFilename%,*,✱))
$set(_albumartistForFilename,$replace(%_albumartistForFilename%,*,✱))
$set(_artistsortForFilename,$replace(%_artistsortForFilename%,*,✱))
$set(_albumartistsortForFilename,$replace(%_albumartistsortForFilename%,*,✱))

$set(_titleForFilename,$replace(%_titleForFilename%,&,＆))
$set(_albumForFilename,$replace(%_albumForFilename%,&,＆))
$set(_discsubtitleForFilename,$replace(%_discsubtitleForFilename%,&,＆))
$set(_artistForFilename,$replace(%_artistForFilename%,&,＆))
$set(_albumartistForFilename,$replace(%_albumartistForFilename%,&,＆))
$set(_artistsortForFilename,$replace(%_artistsortForFilename%,&,＆))
$set(_albumartistsortForFilename,$replace(%_albumartistsortForFilename%,&,＆))
$noop(★ For Development Only - Variable Settings in Subsections ★)
$noop(★ Where Available - Audio Metrics Only at this Time ★)

$noop(########### Audio Metrics Setup  ###########################)
$noop(########### DevMode Values Only ############################)

$set(_devMode,0) $noop(This one is here for convenience, for now this works here, too. But it will need to go later.)

$set(_biitrate,276)
$set(_saample_rate,44100)
$set(_biits_per_sample,16)
$set(_chaannels,2)
$set(_tiitle,My Great Score)
$noop(########### CONFIRM DevMode is Disabled for Live Use ########)
$noop({%title% - %_bitrate% - %_sample_rate% - %_bits_per_sample% - %_channels%})

$if($eq(%_devMode%,1),$set(_bitRateValue,$left(%_biitrate%,3)),$set(_bitRateValue,$left(%_bitrate%,3)))
$if($eq(%_devMode%,1),$set(_bitRateSpeed,%_saample_rate%KHz ),$set(_bitRateSpeed,%_sample_rate%KHz ))
$if($eq(%_devMode%,1),$set(_bitsPerSample,[%_biits_per_sample%]bit ),$set(_bitsPerSample,[%_bits_per_sample%]bit ))
$if($eq(%_devMode%,1),$set(_audioChannels,%_chaannels%ch),$set(_audioChannels,%_channels%ch))
$if($eq(%_devMode%,1),$set(_titleForFilename,%title%),$set(_titleForFilename,%title%))

$noop({%title% - %_bitRateValue% - %_bitRateSpeed% - %_bitsPerSample% - %_audioChannels% - %_titleForFilename% - %_fileCBRRate% - %_fileVBRRate% -  %_bitrate% - %_biitrate%})

$noop(Bitrate factors of 8.0 are CBR, Anything else is VBR)

$set(_bitRateType,$if($eq_any(%_bitRateValue%,320,256,224,192,160,128,112,96,80,64,56,48,40,32,24,16,8),CBR $set(_cbrRateValue,%_bitRateValue%),VBR $set(_vbrRateValue,%_bitRateValue%)))

$noop(Bitrate factors of 8.0 are most likely CBR with the remainder being VBR)

$if($eq(%_cbrRateValue%,320),$set(_fileCBRRate,320),
$if($eq(%_cbrRateValue%,256),$set(_fileCBRRate,256),
$if($eq(%_cbrRateValue%,224),$set(_fileCBRRate,224),
$if($eq(%_cbrRateValue%,192),$set(_fileCBRRate,192),
$if($eq(%_cbrRateValue%,160),$set(_fileCBRRate,160),
$if($eq(%_cbrRateValue%,128),$set(_fileCBRRate,128),
$if($eq(%_cbrRateValue%,112),$set(_fileCBRRate,112),
$if($eq(%_cbrRateValue%,96),$set(_fileCBRRate,96),
$if($eq(%_cbrRateValue%,80),$set(_fileCBRRate,80),
$if($eq(%_cbrRateValue%,64),$set(_fileCBRRate,64),
$if($eq(%_cbrRateValue%,56),$set(_fileCBRRate,56),
$if($eq(%_cbrRateValue%,48),$set(_fileCBRRate,48),
$if($eq(%_cbrRateValue%,40),$set(_fileCBRRate,40),
$if($eq(%_cbrRateValue%,32),$set(_fileCBRRate,32),
$if($eq(%_cbrRateValue%,24),$set(_fileCBRRate,24),
$if($eq(%_cbrRateValue%,16),$set(_fileCBRRate,16),
$if($eq(%_cbrRateValue%,8),$set(_fileCBRRate,8),
)))))))))))))))))

$if($eq(%_bitRateType%,VBR)$set(_fileVBRRate,%_vbrRateValue% ) ,
$if($gt(%_vbrRateValue%,319),$set(_fileVBRRate,320+ ),
$if($gt(%_vbrRateValue%,220),$set(_fileVBRRate,V0 ),
$if($gt(%_vbrRateValue%,191),$set(_fileVBRRate,V1 ),
$if($gt(%_vbrRateValue%,170),$set(_fileVBRRate,V2 ),
$if($gt(%_vbrRateValue%,150),$set(_fileVBRRate,V3 ),
$if($gt(%_vbrRateValue%,140),$set(_fileVBRRate,V4 ),
$if($gt(%_vbrRateValue%,130),$set(_fileVBRRate,V5 ),
$if($gt(%_vbrRateValue%,120),$set(_fileVBRRate,V6 ),
)))))))))
$noop(######### File Naming Structure Variables Complete #########)

$noop(########## Start File Naming Structure Variables ###########)

$noop(★ Typography on file naming only ★)
$set(_titleForFilename,%title%)
$set(_albumForFilename,%album%)
$set(_discsubtitleForFilename,%discsubtitle%)
$noop(_albumartistForFilename,%albumartist%)
$set(_artistForFilename,%artist%)
$noop(set _albumartistsortForFilename,%albumartistsort%)
$set(artistsortForFilename,%artistsort%)

$if(%albumartistsort%,$set(_albumartistsortForFilename,%albumartistsort%),$set(_albumartistsortForFilename,%artist%))
$if(%albumartist%,$set(_albumartistForFilename,%albumartist%),$set(_albumartistForFilename,%artist%))

$noop(★ Pathname Generation Starts Here ★)

$noop(★ Root level Path ★)
$noop(   root = '/Volumes/Drive/Music/ ... [Destination Directory Setting])


$noop(★ Separate by Format at root directory ★)
$noop(   rootLevelPath/MP3/Artist/Album ...)
$if($eq(%_rootLevelTypeSeparation%,1),$upper(%_extension%),)

$noop(   Earlier Incomplete Separation for Sorting ...)
$if($eq(%_earlierPresortForIncompletes%,1),$if($eq($is_complete(),0),$if($lt($matchedtracks(),%_totalalbumtracks%),# - %_incompleteDirectory%)),$if(%_isIncomplete%,# - %_incompleteDirectory%,))/
$if($eq(%_earlierLevelArtistSeparation%,1),%_artistForFilename%/)

$noop(★ Soundtrack in custom directory ,after soundtracksDirectory?? ★)
$noop(   root/*/Audio Books/Title ...)
$noop(   root/*/Soundtracks/Title ...)
$noop(   root/*/Podcasts/Title ...)
$if(%_isSoundTrack%,%_soundTracksDirectory%$left($swapprefix(%album%,A,An,The),1)/,/
$if(%_isAudiobook%,%_audiobooksDirectory%$left($swapprefix(%album%,A,An,The),1)/,/)
$if(%_isPodcast%,%_podcastDirectory%$left($swapprefix(%album%,A,An,The),1)/,/)

$noop(★ Various in custom directory ★)
$noop(root/<*>/Various)
$if(%_isVarious%,%_variousArtistsDirectory%$left($swapprefix(%album%,A,An,The),1)/,/
	$if(%_isGlobalCompil%,%_compilationsGSubDirectory%$left($swapprefix(%album%,A,An,The),1)/,/)
	$noop(★ Order root by category ★)
	$if($eq(%_orderTypeForRoot%,1),
	$if2(%albumgrouping%,Unknown)
	)/

$noop(★ Order root by artist ★)
$noop(root/<*>/<Last.FM=>/)
$noop(root/<*>/D/)

$if($eq(%_orderTypeForRoot%,2),
	$if($eq(%_orderTypeForArtist%,1),$upper($firstalphachar($if2(%_albumartistForFilename%, %_artistForFilename%),#1)),
	$if($eq(%_orderTypeForArtist%,2),	$if(%_isGlobalCompil%,,$upper($firstalphachar($if2(%_albumartistsortForFilename%, %_artistsortForFilename%),#2)))
	)))/


$noop(★ Artist with first letter of first name ★)
$noop(root/<*>/B/The B-52's)
$if($eq(%_orderTypeForArtist%,1),$if2(%_artistSort%,%_albumartistForFilename%,%_artistForFilename%))/

$noop(★ Artist with first letter of last name ★)
$noop(root/<*>/B/B-52's, The)
$if($eq(%_orderTypeForArtist%,2),$if(%_isGlobalCompil%,,$if2(%_albumartistsortForFilename%,%_artistsortForFilename%)))/


$noop(★ Using Alternate Artists Directory For Covers & Tributes  **Uses Order for Album Artist tag [Field]★)

	$noop(root/<*>/O/Oingo Boingo/[Tributes]/DeadBandsParty)
	$if($eq_all(%albumsort%,%_altArtistSort%,%_isTribute%,1),
	$if2(%_artistSort%,%_albumartistForFilename%,%_artistForFilename%)
	)/

	$noop(root/<*>/D/DEVO/[Covers]/Devolution)
	$if($eq_all(%alsbumsort%,%_altArtistSort%,%_isCover%,1),
	$if2(%_artistSort%,%_albumartistForFilename%,%_artistForFilename%)
	)/
	$noop(★ Organize by type ★)
	$noop(root/<*>/Y/Yes/[Live]/90125 Live)
	$noop(root/<*>/Y/Yes,/90125)
	$if($eq(%_separateByTypeInArtistDirectory%,1),
		$if($eq(%_isArtistCompil%,1),%_compilationsASubDirectory%,
			$if($eq(%_isLive%,1),%_liveSubDirectory%,
				$if($eq(%_isCover%,1),%_coverSubDirectory%,
					$if($eq(%_isTribute%,1),%_tributeSubDirectory%,
						$if($eq(%_isEP%,1),%_epSubDirectory%,
							$if($eq(%_isSingle%,1),%_singlesSubDirectory%,
								$if($eq(%_isBroadcast%,1),%_broadcastSubDirectory%,
									$if($eq(%_isVideo%,1),%_videoSubDirectory%,
										$if($eq(%_isOther%,1),%_otherSubDirectory%,
											$if($eq(%_isAlbum%,1),
											$if($eq(%_separateAlbum%,1),%_albumSubDirectory%))

											))))))))))))

$noop(root/<*>/B/B-52's, The]/Bouncing off the Satellites/ )
%_albumForFilename%
$noop(★ Bouncing off the Satellites [Media-Type]/ ★)
$noop($if($ne(%media%,CD),$if(%media%,[$rreplace(%media%,["″], Inch)])))
$if(%media%, [$title(%media%]),)

$noop($if($and(%media%,$ne(%media%,CD)),$if($in(%media%,Vinyl),$title( [%media%])),$upper( [%media%])))

$noop(★ Bouncing off the Satellites [Vinyl] [YEAR]/ ★)
$if($eq(%_showDate%,1),$if($if2(%date%,%originalyear%,%originaldate%), [$left($if2(%date%,%originalyear%,%originaldate%),4)], [0000]))
$noop(★ Bouncing off the Satellites [Vinyl] [1986] [Release Status]/ ★)
$if(%releasestatus%,$if($eq(%_showReleaseStatus%,1),$title( [%releasestatus%])))

$noop(★ Bouncing off the Satellites [Vinyl] [1986] [Official] [Label]/ ★)
$if(%label%,$if(%_showRecordLabel%, $if(%label%,$title([%label%]))))

$noop(★ Bouncing off the Satellites [Vinyl] [1986] [Official] [MCA] [CAT-Number]/ ★)
$if(%catalognumber%,$if($eq(%_showCatalogueNumber%,1),$title( [%catalognumber%])))

$noop(★ Bouncing off the Satellites [Vinyl] [1986] [Official] [MCA] [AB-DC001]/ ★)
$noop(★ Bouncing off the Satellites [Vinyl] [1986] [Official] [MCA] [AB-DC001] - Incomplete/ ★)
$if($eq(%_extraTrackHandling%,1),$if($eq($is_complete(),0),$if($lt($matchedtracks( ),%_totalalbumtracks%), - %_incompleteDirectory%)),$if(%_isIncomplete%, - %_incompleteDirectory%,))/

$noop(★ Bouncing off the Satellites [Vinyl] [1986] [Official] [MCA] [AB-DC001]/ MP3 / ★)
$noop(★ Bouncing off the Satellites [Vinyl] [1986] [Official] [MCA] [AB-DC001]/ Bouncing off the Satellites MP3 / ★)
$if($eq(%_albumLevelTypeSeparation%,1),$if($eq(%_albumNameAtTypeSeparation%,1),%_albumForFilename% ,)$upper(%_extension%))/

$noop(★ One Last Option to Sort By Author -winthin- a Left Side Album Compilation/ ★)
$if(%artist%,$if($eq(%_showTrackArtistSeparation%,1),$title(%artist%)))


$noop(★ Bouncing off the Satellites [Vinyl] [1986] [Official] [MCA] [AB-DC001]/ .../ Disc # ★)
$if($gt(%totaldiscs%,1),$noop(
	)$if($lt(%totaldiscs%,10),$set(_discnumber, %discnumber%),$set(_discnumber,$num(%discnumber%,2)))$noop(
	)$if($in(%media%,Vinyl),$noop(
		)$set(_nameForDiscDirectory,@OSLASH@@OBRACKET@%_nameForTypeVinyl%%_discnumber%@CBRACKET@),$noop(
		)$set(_nameForDiscDirectory,@OSLASH@@OBRACKET@%_nameForTypeCD%%_discnumber%@CBRACKET@))$noop(
		)$if($and(%_discsubtitleForFilename%,$eq(%_showDiscSubtitle%,1)),$set(_nameForDiscDirectory,%_nameForDiscDirectory% - %_discsubtitleForFilename%))$noop(
		)$if($eq(%_useSubDiscDirectory%,1),$noop(
			)$set(_nameForDiscDirectory,$replace(%_nameForDiscDirectory%,@OSLASH@@OBRACKET@,/))$noop(
			)$set(_nameForDiscDirectory,$replace(%_nameForDiscDirectory%,@CBRACKET@,)),$noop(
			)$if($eq(%_mergeDiscWhenNotUsingSubDirectory%,1),$noop(
				)$unset(_nameForDiscDirectory),$noop(
				)$set(_nameForDiscDirectory,$replace(%_nameForDiscDirectory%,@OSLASH@@OBRACKET@,[))$noop(
			)$set(_nameForDiscDirectory,$replace(%_nameForDiscDirectory%,@CBRACKET@,]))$noop(
		))$noop(
	))$noop(
)$if(%_nameForDiscDirectory%,%_nameForDiscDirectory%))/

$noop(★ Track # Title --%_filebr% -- %bitrate% -- %BRType% -- %BrVBR% --  ★)
$if($in(%media%,Vinyl),$noop(
	)$if($eq(%_useMusicBrainzStyleForVinylTrack%,1),$noop(
		)$if(%_musicbrainz_tracknumber%,%_musicbrainz_tracknumber%. )$noop(
	)),$noop(
	)$if(%tracknumber%,$if($gt(%totaldiscs%,1),$if($and($eq(%_useSubDiscDirectory%,0),$eq(%_mergeDiscWhenNotUsingSubDirectory%,1)),%discnumber%))$num(%tracknumber%,2). ))

$noop(★ GAME OVER ★)
%_titleForFilename%
$if($eq(%_showTime%,1),[%_length%] )
$if($eq(%_showBandwidth%,1),[%_fileCBRRate%%_fileVBRRate%%_bitRateSpeed%%_bitRateType%%_audioChannels%])

$noop(★ 00 CREDITS ★)
