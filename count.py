    punch = 0
    clip_presence = 0
    clip_absence = 0
    toggle_bar_presence = 0
    toggle_bar_absence = 0
    print_damage = 0
    improper_printing = 0
    proper_printing = 0
    screw = 0
    counter_img = 0
for *xyxy, conf, cls in reversed(det):   #coordinates
                    if save_txt:  
                        xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  
                        line = (cls, *xywh, conf) if save_conf else (cls, *xywh)  
                        with open(txt_path + '.txt', 'a') as f:
                            f.write(('%g ' * len(line)).rstrip() % line + '\n')

                    if save_img or save_crop or view_img:  
                        c = int(cls)  
                        label = None if hide_labels else (names[c] if hide_conf else f'{names[c]} {conf:.2f}')
                        temp1 = path.split('/')[-1].split('.')[0]
                        temp1 = temp1.split('_')[0]
                        label1 = label[1:]



                        if 'punch' in label:
                            punch += 1
                        elif 'clip_presence' in label:
                            clip_presence +=1 
                        elif 'clip_absence' in label:
                            clip_absence +=1 
                        elif 'toggle_bar_presence' in label:
                            toggle_bar_presence +=1 
                        elif 'toggle_bar_absence' in label:
                             toggle_bar_absence +=1
                        elif 'print_damage' in label:
                              print_damage +=1
                        elif 'improper_printing' in label:
                             improper_printing +=1
                        elif 'proper_printing' in label:
                             proper_printing +=1
                        elif 'screw' in label:
                              screw +=1                         
                        else:
                            pass

                        

                    
                        label = temp1+'_'+label[1:]  #croping label

                        annotator.box_label(xyxy, label, color=colors(c, True))
                        if save_crop:
                            save_one_box(xyxy, imc, file=save_dir / 'crops' / names[c] / f'{p.stem}.jpg', BGR=True)
            temp = punch + clip_presence + clip_absence + toggle_bar_presence + toggle_bar_absence + print_damage + improper_printing + proper_printing + screw
            t1 = punch
            t2 = clip_presence
            t3 = clip_absence
            t4 = toggle_bar_presence
            t5 = toggle_bar_absence
            t6 = print_damage
            t7 = improper_printing
            t8 = proper_printing
            t9 = screw
            def Convert(x):
                n = iter(x)
                n = dict(zip(n, n))
                return n
            x = ["Total Detections of punch" , t1,"Total Detections of clip_presence",t2 ,"Total Detections of clip_absence",t3 , 'toggle_bar_presence',t4 , 'toggle_bar_absence',t5 ,'print_damage',t6 , 'improper_printing',t7 , 'proper_printing',t8 , 'screw',t9]
            print(Convert(x))
            print(f'Total No.Of Images: {counter_img} \n Image not detected : {counter_img - temp}')