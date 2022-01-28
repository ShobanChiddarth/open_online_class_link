import configparser, datetime

# Reading 'timetable.txt'
timetablefile=open('timetable.txt','r')


# first line stored in `timings`
for line in timetablefile:
    timings=line
    break



# process timings

timings=timings.split('|')
del timings[0]
del timings[0]
del timings[-1]
for timing in range(len(timings)):
    timings[timing]=timings[timing].split('-')

for ii in range(len(timings)):
    for jj in range(len(timings[ii])):
        timings[ii][jj] = timings[ii][jj].strip()

for kk in range(len(timings)):
    for ll in range(len(timings[kk])):
        timings[kk][ll] = eval(timings[kk][ll])

for lst in range(len(timings)):
    timings[lst]=tuple(timings[lst])


# Ignore Line 2 as it is empty
for line in timetablefile:
    pass
    break

# reading all the lines
DAYS = [line for line in timetablefile]
# processing DAYS
for iday in range(len(DAYS)):
   DAYS[iday]=DAYS[iday].split('|')
   del DAYS[iday][0]
   del DAYS[iday][0]
   del DAYS[iday][-1]
   for v in range(len(DAYS[iday])):
       for w in range(len(DAYS[iday][v])):
               DAYS[iday][v]=DAYS[iday][v].strip()


# Read 'links.ini'
link = configparser.ConfigParser()
link.read('links.ini')
a,b=[],[]
for subject in link['Subjects']:
    a.append(subject.upper())
    b.append(link['Subjects'][subject])
links=dict(zip(a, b))
links['noclass']='noclass'

# Date and Time
now    = datetime.datetime.now()
day    = now.strftime('%A').upper()
hour   = now.hour
minute = now.minute
time   = (hour, minute)


# change it according to your timetable, like if you had classes on Sundays.
periods={'MONDAY':DAYS[0],
        'TUESDAY':DAYS[1], 
        'WEDNESDAY':DAYS[2], 
        'THURSDAY':DAYS[3], 
        'FRIDAY':DAYS[4], 
        'SATURDAY':DAYS[5],
        'SUNDAY':'noclass',
        'noclass':'noclass'}



# finale
if periods[day] != 'noclass':

    inside=False # if current time is inside timings (first line in 'timetable.txt')
    c=0
    for start, stop in timings:
        if start <= time < stop:
            inside=True
            break
        c+=1

    if inside:
        PERIOD=periods[day][c]
        LINK=links[PERIOD]

else:
    PERIOD=periods[day]
    LINK=links[PERIOD]