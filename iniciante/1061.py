dia_str_i, dia_int_i = map(str, input().split())
hh_i, mm_i, ss_i = map(int, input().split(':'))

dia_str_t, dia_int_t = input().split()
hh_t, mm_t, ss_t = map(int, input().split(':'))

dia_int_i = int(dia_int_i)
dia_int_t = int(dia_int_t)

dia_seg = int(86400)
hora_seg = int(3600)
min_seg = int(60)

seg_total_i = ((dia_int_i * dia_seg) + (hh_i * hora_seg) + (mm_i * min_seg) + (ss_i))
seg_total_t = ((dia_int_t * dia_seg) + (hh_t * hora_seg) + (mm_t * min_seg) + (ss_t))

seg_total_dif = (seg_total_t - seg_total_i)

dia_dif = (seg_total_dif // dia_seg)
r_dia_dif = (seg_total_dif % dia_seg)
hora_dif = (r_dia_dif // hora_seg)
r_hora_dif = (r_dia_dif % hora_seg)
min_dif = (r_hora_dif // min_seg)
r_min_dif = (r_hora_dif % min_seg)
seg_dif = (r_hora_dif % min_seg)

print(f'{dia_dif} dia(s)')
print(f'{hora_dif} hora(s)')
print(f'{min_dif} minuto(s)')
print(f'{seg_dif} segundo(s)')