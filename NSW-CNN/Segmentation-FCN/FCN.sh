#!usr/bin

save_dir=./Result/FCN/
job_cnt=0


epoch=20
POS=0
for CONV in "16-32-64-128"; do
    for OUT_CONV in "3"; do
        for catIn in "0" "1-16|1-32"; do
            for NORM in m G ; do
                for RAND in 0; do

                    # weighted
                    name=FCN_${CONV}_${OUT_CONV}_${NORM}_weight_p${POS}_e${epoch}_r${RAND}
                    python FCN.py --conv ${CONV} --output_conv ${OUT_CONV} --concat_input ${catIn} --norm ${NORM} --pos ${POS} --save ${save_dir} --record_summary --rand ${RAND} --gpu ${RAND} --epoch ${epoch} >./Log/FCN/${name}  2>&1
                    echo ${name}

                    # weighted, batch norm
                    name=FCN_${CONV}_${OUT_CONV}_${NORM}_weight_bn_p${POS}_e${epoch}_r${RAND}
                    python FCN.py --conv ${CONV} --output_conv ${OUT_CONV} --concat_input ${catIn} --norm ${NORM} --pos ${POS} --save ${save_dir} --record_summary --rand ${RAND} --gpu ${RAND} --epoch ${epoch} --use_batch_norm >./Log/FCN/${name}  2>&1
                    echo ${name}

                    sleep 10m
                    job_cnt=$((job_cnt+2))
                    if [ $(($job_cnt%6)) -eq 0 ]; then
                        wait
                    fi
                done
            done
        done
    done
done
