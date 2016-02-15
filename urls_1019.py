urls = [
"http://www.cars.com/for-sale/searchresults.action?feedSegId=28705&sf2Nm=price&requestorTrackingInfo=RTB_SEARCH&sf1Nm=actualPhotoCount&sf2Dir=DESC&PMmt=1-1-0&zc=92612&rd=100000&mdId=48263&mkId=20005&sf1Dir=DESC&searchSource=UTILITY&crSrtFlds=feedSegId-mkId-mdId&pgId=2102&rpp=100",
"http://www.cars.com/for-sale/searchresults.action?feedSegId=28705&sf2Nm=price&requestorTrackingInfo=RTB_SEARCH&yrId=34923&yrId=39723&sf1Nm=actualPhotoCount&sf2Dir=DESC&stkTypId=28881&PMmt=1-1-0&zc=92612&rd=200&mdId=20800&mkId=20088&sf1Dir=DESC&searchSource=UTILITY&crSrtFlds=stkTypId-feedSegId-mkId-mdId&pgId=2102&rpp=100",
"http://www.cars.com/for-sale/searchresults.action?feedSegId=28705&sf2Nm=price&requestorTrackingInfo=RTB_SEARCH&yrId=56007&sf1Nm=actualPhotoCount&sf2Dir=DESC&stkTypId=28881&PMmt=1-1-0&zc=92612&rd=200&mdId=20800&mkId=20088&sf1Dir=DESC&searchSource=UTILITY&crSrtFlds=stkTypId-feedSegId-mkId-mdId&pgId=2102&rpp=100",
"http://www.cars.com/for-sale/searchresults.action?feedSegId=28705&sf2Nm=price&requestorTrackingInfo=RTB_SEARCH&yrId=58487&sf1Nm=actualPhotoCount&sf2Dir=DESC&PMmt=1-1-0&zc=92612&rd=200&mdId=20823&mkId=20017&sf1Dir=DESC&searchSource=UTILITY&crSrtFlds=feedSegId-mkId-mdId&pgId=2102&rpp=100",
]


import pickle

batch_size = len(urls) / 1
for x in range(0, len(urls), batch_size):
	sub_arr = urls[x:x+batch_size]
	pickle.dump (sub_arr, open('urls_%d.p' %(x/batch_size), 'wb'))

# import glob, pickle
# test = []
# for x in glob.glob ('*.p'):
# 	for y in pickle.load(open(x, 'rb')):
# 		test.append (y)
# print len (test)
# print set(urls).difference(set(test))
