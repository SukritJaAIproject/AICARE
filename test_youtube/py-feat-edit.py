def detect_image(self, frame, outputFname=None, verbose=False):
    self.info["inputFname"] = 'inputFname'

    init_df = pd.DataFrame(columns=self["output_columns"])
    if outputFname:
        init_df.to_csv(outputFname, index=False, header=True)

    if verbose:
        print(f"processing {inputF}")
    # frame = cv2.imread(inputF)
    df = self.process_frame(frame)
    df["input"] = inputF
    if outputFname:
        df[init_df.columns].to_csv(
            outputFname, index=False, header=False, mode="a"
        )
    else:
        init_df = pd.concat([init_df, df[init_df.columns]], axis=0)

    if outputFname:
        return True
    else:
        return Fex(
            init_df,
            filename='inputFname',
            au_columns=self['au_presence_columns'],
            emotion_columns=FEAT_EMOTION_COLUMNS,
            facebox_columns=FEAT_FACEBOX_COLUMNS,
            landmark_columns=openface_2d_landmark_columns,
            time_columns=FACET_TIME_COLUMNS,
            detector="Feat",
        )
