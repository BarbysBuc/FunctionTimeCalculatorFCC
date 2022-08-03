def add_time(start, duration, day = ""):
  #dias de la semana
  week_dict = {'Monday': 1,'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}
  
  
  #Preparing the elements
  start_hr, start_min = start.split(':')
  start_min, t = start_min.split() #AM or PM
  t = t.upper()
  new_t = t
 
  duration_hr, duration_min = duration.split(':')
  start_hr = int(start_hr)
  start_min = int(start_min)
  duration_hr = int(duration_hr)
  duration_min = int(duration_min)

  #adding min
  new_min = start_min + duration_min
  if new_min > 59:#checking if need to convert to hour
    start_hr += 1 
    new_min = new_min % 60
  if new_min < 10:
    new_min = '0'+ str(new_min)
def add_time(start, duration, day = ""):
  #dias de la semana
  week_dict = {'Monday': 1,'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}
  
  
  #Preparing the elements
  start_hr, start_min = start.split(':')
  start_min, t = start_min.split() #AM or PM
  t = t.upper()
  new_t = t
 
  duration_hr, duration_min = duration.split(':')
  start_hr = int(start_hr)
  start_min = int(start_min)
  duration_hr = int(duration_hr)
  duration_min = int(duration_min)

  #adding min
  new_min = start_min + duration_min
  if new_min > 59:#checking if need to convert to hour
    start_hr += 1 
    new_min = new_min % 60
  if new_min < 10:
    new_min = '0'+ str(new_min)
  #adding hours
  new_hr = start_hr + duration_hr
  #checking days passed
  add_day = 0
  if new_hr > 24:
    add_day = new_hr // 24
    new_hr = new_hr % 24
  #checking for am or pm
  if new_hr > 12 and t == 'AM':
    new_hr = new_hr % 12
    new_t = 'PM'
    
  elif new_hr > 12 and t == 'PM':
    add_day += 1
    new_hr = new_hr % 12
    new_t = 'AM'
  elif new_hr == 12 and t == 'PM':
    add_day += 1
    new_t = 'AM'
  elif new_hr == 12 and t == 'AM':
    new_t = 'PM'
  new_t = new_t.strip(' ')  
  #structuring return
  new_time = f'{new_hr}:{new_min} {new_t}'
  if day:
    day = day.capitalize()
    weekday = week_dict[day] + add_day
    if weekday > 7:
      weekday = weekday % 7
    for d, n in week_dict.items():
      if n == weekday:
        new_day = d.rstrip()
    
    if day == new_day and add_day == 0:
      new_time = f'{new_time}, {new_day}'
      return new_time
    elif day != new_day and add_day == 1:
      text = '(next day)'
      text = text.strip(' ')
      return f'{new_time}, {new_day}{text}'
       
    else:
      new_time = f'{new_time}, {new_day} ({add_day} days later)'
      return new_time

  if t == new_t and add_day == 0:
    return new_time
  elif t == 'AM' and t != new_t and add_day == 0:
    return new_time
  elif t == 'PM' and t != new_t and add_day == 1:
    text = '(next day)'
    text = text.strip(' ')
    return f'{new_time}{text}'
  elif t == 'AM' and t == new_t and add_day == 1:
    return f'{new_time}(next day)'
  
  else :
    new_time = f'{new_time} ({add_day} days later)'
    return new_time