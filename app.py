import streamlit as st
from jreadability import compute_readability

st.set_page_config(
    page_title='jReadability demo',
    page_icon='favicon.svg',
)

st.markdown("[Code for jreadability python [package](https://github.com/joshdavham/jreadability) and [demo](https://github.com/joshdavham/jreadability-demo)]")

lower_intermediate_text = "茶々はわたしの日本語の先輩でした。毎日、日本語を一生懸命勉強して3か月ぐらいたったころには、日本人の友達といろいろな話もできるようになりました。そして茶々よりも日本語がわかるようになりました。けれどわたしの日本語の発音はまだ上手ではありません。家の人はわかってくれますが、茶々はわかりません。「おいで」と言っても茶々は来ません。「ちょっと見てごらん」と言っても見ません。「散歩に行こう」と言ってもふりむいてくれません。だから、いっしょに散歩することもできません。わたしの発音が家の人とちがうからです。それが大変ざんねんでした。それで、わたしはテープをたくさん聞いて練習しました。そして、はじめて茶々がわたしの「おいで」を聞いて、わたしのところへ来てくれた時は、本当にうれしくなりました。\
    わたしの日本語がやっと茶々につうじたからです。今は、わたしは日本の生活にだいぶなれました。茶々はもう、わたしの日本語が大体わかりますから、毎日いっしょに散歩します。わたしの日本語の先輩、茶々のおかげで日本語も上手になったし、犬がこわくなくなって、犬が好きになりました。今度、わたしは茶々に中国語を教えようと思います。そして、中国語と日本語と、二つのことばのわかる犬にするつもりです。"

st.image("logo.svg", use_column_width=False, width=350)

text = st.text_area(
    label="Input Japanese text below and then click the button",
    label_visibility='visible',
    height=350,
    max_chars=None,
    key='text-input',
    placeholder='Enter a paragraph of Japanese text.',
    value = lower_intermediate_text,
)

if st.button("Compute readability"):

    if text:

        score = compute_readability(text)

        if 0.5 <= score < 6.5:

            if 0.5 <= score < 1.5:
                st.error(f"Readability score: **{score:.2f}**  \nLevel: **Upper-advanced**")
            elif 1.5 <= score < 2.5:
                st.error(f"Readability score: **{score:.2f}**  \nLevel: **Lower-advanced**")
            elif 2.5 <= score < 3.5:
                st.info(f"Readability score: **{score:.2f}**  \nLevel: **Upper-intermediate**")
            elif 3.5 <= score < 4.5:
                st.info(f"Readability score: **{score:.2f}**  \nLevel: **Lower-intermediate**")
            elif 4.5 <= score < 5.5:
                st.success(f"Readability score: **{score:.2f}**  \nLevel: **Upper-elementary**")
            elif 5.5 <= score < 6.5:
                st.success(f"Readability score: **{score:.2f}**  \nLevel: **Lower-elementary**")

            st.progress(1-((score - 0.5) / 6.0) )

        else:

            st.warning(f"Readability score: **{score:.2f}**  \nLevel: **Undefined**") 

    else:

        st.info(f"Readability score:  \nLevel:")
        st.progress(0.0)

else:

    st.info(f"Readability score:  \nLevel:")
    st.progress(0.0)

st.markdown("---")

st.markdown(
    """         
    ## Readability scores

    | Level              | Readability score range |
    |--------------------|-------------------------|
    | Upper-advanced     | [0.5, 1.5)                 |
    | Lower-advanced     | [1.5, 2.5)               |
    | Upper-intermediate | [2.5, 3.5)               |
    | Lower-intermediate | [3.5, 4.5)               |
    | Upper-elementary   | [4.5, 5.5)               |
    | Lower-elementary   | [5.5, 6.5)               |
    """
)

st.markdown(
    """
    ### Model

    ```
    readability = {mean number of words per sentence} * -0.056
                + {percentage of kango} * -0.126
                + {percentage of wago} * -0.042
                + {percentage of verbs} * -0.145
                + {percentage of particles} * -0.044
                + 11.724
    ```

    *\* "kango" (漢語) means Japanese word of Chinese origin while "wago" (和語) means native Japanese word.*

    """
)

st.markdown("---")

st.markdown(
    """
    ### About

    This website simply serves as a demo of the [jreadability python package](https://github.com/joshdavham/jreadability) which is an unofficial implementation of the model developed by 
    Jae-ho Lee and Yoichiro Hasebe in [Introducing a readability evaluation system for Japanese language education](https://jreadability.net/file/hasebe-lee-2015-castelj.pdf) 
    and [Readability measurement of Japanese texts based on levelled corpora](https://researchmap.jp/jhlee/published_papers/21426109).

    This website is also heavily inspired from the official [jreadability.net](https://jreadability.net/sys/en) (which is a much better site!)
    
    As for why I built this demo, I was just inspired by Paul O'Leary McCann's [demo](https://fugashi.streamlit.app/) of [fugashi](https://github.com/polm/fugashi) and thought it'd be cool if more python packages had demos like that.
    """
)