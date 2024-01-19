# create a manifest that kills a process named killmenow

exec {'use a commend'
  command => 'pkill killmenow'
}
