import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)

# Navbar HTML
navbar_html = '''
<style>
    .st-emotion-cache-12fmjuu{
        z-index: 100;
    }
    .st-emotion-cache-h4xjwg{
        z-index: 100;
    }
    h2{
    color: white;
    }
    .css-hi6a2p {padding-top: 0rem;}
    .navbar {
        background-color: #355E3B;
        padding: 0.3rem;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 1000;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .navbar .logo {
        display: flex;
        align-items: center;
    }
    .navbar .logo img {
        height: 40px;
        margin-right: 10px;
    }
    .navbar .menu {
        display: flex;
        gap: 1.5rem;
    }
    .navbar .menu a {
        color: white;
        font-size: 1.2rem;
        text-decoration: none;
    }
    .content {
        padding-top: 5rem;  /* Adjust this based on navbar height */
    }
</style>

<nav class="navbar">
    <div class="logo">
        <svg height="80" viewBox="0 0 1629 307" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect y="2" width="1577" height="305" rx="27" fill="white"/>
<line x1="291" y1="184" x2="871.003" y2="184" stroke="black" stroke-width="8"/>
<path d="M292.544 253H288.312V220.064H292.544L303.998 240.12H304.182L315.636 220.064H319.868V253H315.636V233.45L315.82 227.93H315.636L305.332 246.008H302.848L292.544 227.93H292.36L292.544 233.45V253ZM352.45 253H348.402V249.872H348.218C347.574 250.976 346.578 251.896 345.228 252.632C343.91 253.368 342.53 253.736 341.088 253.736C338.328 253.736 336.197 252.954 334.694 251.39C333.222 249.795 332.486 247.541 332.486 244.628V230.46H336.718V244.352C336.81 248.032 338.666 249.872 342.284 249.872C343.971 249.872 345.382 249.197 346.516 247.848C347.651 246.468 348.218 244.827 348.218 242.926V230.46H352.45V253ZM369.194 220.064V253H364.962V220.064H369.194ZM390.859 253.368C389.019 253.368 387.486 252.801 386.259 251.666C385.063 250.531 384.45 248.952 384.419 246.928V234.324H380.463V230.46H384.419V223.56H388.651V230.46H394.171V234.324H388.651V245.548C388.651 247.051 388.943 248.078 389.525 248.63C390.108 249.151 390.767 249.412 391.503 249.412C391.841 249.412 392.163 249.381 392.469 249.32C392.807 249.228 393.113 249.121 393.389 248.998L394.723 252.77C393.619 253.169 392.331 253.368 390.859 253.368ZM411.256 222.686C411.256 223.514 410.964 224.219 410.382 224.802C409.799 225.385 409.094 225.676 408.266 225.676C407.438 225.676 406.732 225.385 406.15 224.802C405.567 224.219 405.276 223.514 405.276 222.686C405.276 221.858 405.567 221.153 406.15 220.57C406.732 219.987 407.438 219.696 408.266 219.696C409.094 219.696 409.799 219.987 410.382 220.57C410.964 221.153 411.256 221.858 411.256 222.686ZM410.382 230.46V253H406.15V230.46H410.382ZM437.969 240.488H423.249V236.992H437.969V240.488ZM460.585 249.872C462.67 249.872 464.372 249.121 465.691 247.618C467.071 246.115 467.761 244.153 467.761 241.73C467.761 239.369 467.071 237.421 465.691 235.888C464.341 234.355 462.639 233.588 460.585 233.588C458.561 233.588 456.859 234.355 455.479 235.888C454.099 237.421 453.409 239.369 453.409 241.73C453.409 244.122 454.099 246.069 455.479 247.572C456.859 249.105 458.561 249.872 460.585 249.872ZM459.895 253.736C456.951 253.736 454.421 252.571 452.305 250.24C450.219 247.879 449.177 245.042 449.177 241.73C449.177 238.418 450.219 235.581 452.305 233.22C454.421 230.889 456.951 229.724 459.895 229.724C461.551 229.724 463.053 230.077 464.403 230.782C465.783 231.487 466.841 232.423 467.577 233.588H467.761L467.577 230.46V220.064H471.809V253H467.761V249.872H467.577C466.841 251.037 465.783 251.973 464.403 252.678C463.053 253.383 461.551 253.736 459.895 253.736ZM488.56 253H484.328V230.46H488.376V234.14H488.56C488.99 232.944 489.864 231.932 491.182 231.104C492.532 230.245 493.85 229.816 495.138 229.816C496.365 229.816 497.408 230 498.266 230.368L496.978 234.462C496.457 234.247 495.629 234.14 494.494 234.14C492.9 234.14 491.504 234.784 490.308 236.072C489.143 237.36 488.56 238.863 488.56 240.58V253ZM528.179 253H524.131V249.872H523.947C523.303 250.976 522.307 251.896 520.957 252.632C519.639 253.368 518.259 253.736 516.817 253.736C514.057 253.736 511.926 252.954 510.423 251.39C508.951 249.795 508.215 247.541 508.215 244.628V230.46H512.447V244.352C512.539 248.032 514.395 249.872 518.013 249.872C519.7 249.872 521.111 249.197 522.245 247.848C523.38 246.468 523.947 244.827 523.947 242.926V230.46H528.179V253ZM550.586 249.872C552.672 249.872 554.374 249.121 555.692 247.618C557.072 246.115 557.762 244.153 557.762 241.73C557.762 239.369 557.072 237.421 555.692 235.888C554.343 234.355 552.641 233.588 550.586 233.588C548.562 233.588 546.86 234.355 545.48 235.888C544.1 237.421 543.41 239.369 543.41 241.73C543.41 244.122 544.1 246.069 545.48 247.572C546.86 249.105 548.562 249.872 550.586 249.872ZM550.448 263.672C549.191 263.672 548.01 263.503 546.906 263.166C545.802 262.859 544.79 262.415 543.87 261.832C542.981 261.249 542.214 260.559 541.57 259.762C540.926 258.965 540.436 258.075 540.098 257.094L544.1 255.438C544.56 256.757 545.358 257.815 546.492 258.612C547.627 259.409 548.946 259.808 550.448 259.808C552.748 259.808 554.542 259.118 555.83 257.738C557.118 256.358 557.762 254.457 557.762 252.034V249.872H557.578C556.781 251.068 555.692 252.019 554.312 252.724C552.963 253.399 551.491 253.736 549.896 253.736C546.952 253.736 544.422 252.586 542.306 250.286C540.221 247.925 539.178 245.073 539.178 241.73C539.178 238.387 540.221 235.551 542.306 233.22C544.422 230.889 546.952 229.724 549.896 229.724C551.491 229.724 552.963 230.077 554.312 230.782C555.692 231.457 556.781 232.392 557.578 233.588H557.762V230.46H561.81V252.034C561.81 255.653 560.783 258.489 558.728 260.544C556.643 262.629 553.883 263.672 550.448 263.672ZM611.762 220.064V224.112H596.766V234.554H610.29V238.51H596.766V248.952H611.762V253H592.534V220.064H611.762ZM645.157 244.214C645.157 247.097 644.099 249.412 641.983 251.16C639.837 252.877 637.23 253.736 634.163 253.736C631.434 253.736 629.027 252.939 626.941 251.344C624.856 249.749 623.415 247.572 622.617 244.812L626.665 243.156C626.941 244.137 627.325 245.027 627.815 245.824C628.306 246.621 628.873 247.311 629.517 247.894C630.192 248.446 630.928 248.891 631.725 249.228C632.523 249.535 633.366 249.688 634.255 249.688C636.187 249.688 637.767 249.197 638.993 248.216C640.22 247.204 640.833 245.87 640.833 244.214C640.833 242.834 640.327 241.653 639.315 240.672C638.365 239.721 636.586 238.801 633.979 237.912C631.342 236.961 629.701 236.317 629.057 235.98C625.561 234.201 623.813 231.579 623.813 228.114C623.813 225.691 624.779 223.621 626.711 221.904C628.674 220.187 631.081 219.328 633.933 219.328C636.448 219.328 638.625 219.972 640.465 221.26C642.305 222.517 643.532 224.097 644.145 225.998L640.189 227.654C639.821 226.427 639.085 225.415 637.981 224.618C636.908 223.79 635.589 223.376 634.025 223.376C632.369 223.376 630.974 223.836 629.839 224.756C628.705 225.615 628.137 226.734 628.137 228.114C628.137 229.249 628.582 230.23 629.471 231.058C630.453 231.886 632.584 232.867 635.865 234.002C639.208 235.137 641.585 236.532 642.995 238.188C644.437 239.813 645.157 241.822 645.157 244.214ZM676.517 220.064H681.991V220.248L669.755 234.37L682.819 252.816V253H677.621L666.903 237.636L661.843 243.478V253H657.611V220.064H661.843V237.038H662.027L676.517 220.064ZM705.546 225.262L700.164 240.12H711.112L705.73 225.262H705.546ZM695.518 253H690.826L703.246 220.064H708.03L720.45 253H715.758L712.584 244.076H698.738L695.518 253ZM735.905 239.66V253H731.673V220.064H742.897C745.749 220.064 748.172 221.015 750.165 222.916C752.189 224.817 753.201 227.133 753.201 229.862C753.201 232.653 752.189 234.983 750.165 236.854C748.202 238.725 745.78 239.66 742.897 239.66H735.905ZM735.905 224.112V235.612H742.989C744.676 235.612 746.071 235.045 747.175 233.91C748.31 232.775 748.877 231.426 748.877 229.862C748.877 228.329 748.31 226.995 747.175 225.86C746.071 224.695 744.676 224.112 742.989 224.112H735.905ZM784.226 220.064V224.112H769.23V234.554H782.754V238.51H769.23V248.952H784.226V253H764.998V220.064H784.226ZM816.517 220.064V224.112H801.521V234.554H815.045V238.51H801.521V248.952H816.517V253H797.289V220.064H816.517ZM851.281 224.112V235.704H858.089C859.806 235.704 861.263 235.152 862.459 234.048C863.655 232.913 864.253 231.518 864.253 229.862C864.253 228.329 863.685 226.995 862.551 225.86C861.447 224.695 860.051 224.112 858.365 224.112H851.281ZM851.281 253H847.049V220.064H858.273C861.125 220.064 863.547 221.015 865.541 222.916C867.565 224.787 868.577 227.102 868.577 229.862C868.577 232.131 867.825 234.155 866.323 235.934C864.851 237.682 862.98 238.801 860.711 239.292L860.619 239.43L869.865 252.816V253H864.851L855.973 239.66H851.281V253ZM889.937 253.736C886.625 253.736 883.896 252.601 881.749 250.332C879.602 248.063 878.529 245.195 878.529 241.73C878.529 238.295 879.572 235.443 881.657 233.174C883.742 230.874 886.41 229.724 889.661 229.724C893.004 229.724 895.656 230.813 897.619 232.99C899.612 235.137 900.609 238.157 900.609 242.052L900.563 242.512H882.853C882.914 244.72 883.65 246.499 885.061 247.848C886.472 249.197 888.158 249.872 890.121 249.872C892.82 249.872 894.936 248.523 896.469 245.824L900.241 247.664C899.229 249.565 897.818 251.053 896.009 252.126C894.23 253.199 892.206 253.736 889.937 253.736ZM883.175 239.016H896.101C895.978 237.452 895.334 236.164 894.169 235.152C893.034 234.109 891.501 233.588 889.569 233.588C887.974 233.588 886.594 234.079 885.429 235.06C884.294 236.041 883.543 237.36 883.175 239.016ZM929.314 246.744C929.314 248.707 928.455 250.363 926.738 251.712C925.02 253.061 922.858 253.736 920.252 253.736C917.982 253.736 915.989 253.153 914.272 251.988C912.554 250.792 911.328 249.228 910.592 247.296L914.364 245.686C914.916 247.035 915.713 248.093 916.756 248.86C917.829 249.596 918.994 249.964 920.252 249.964C921.601 249.964 922.72 249.673 923.61 249.09C924.53 248.507 924.99 247.817 924.99 247.02C924.99 245.579 923.886 244.521 921.678 243.846L917.814 242.88C913.428 241.776 911.236 239.66 911.236 236.532C911.236 234.477 912.064 232.837 913.72 231.61C915.406 230.353 917.553 229.724 920.16 229.724C922.153 229.724 923.947 230.199 925.542 231.15C927.167 232.101 928.302 233.373 928.946 234.968L925.174 236.532C924.744 235.581 924.039 234.845 923.058 234.324C922.107 233.772 921.034 233.496 919.838 233.496C918.734 233.496 917.737 233.772 916.848 234.324C915.989 234.876 915.56 235.551 915.56 236.348C915.56 237.636 916.771 238.556 919.194 239.108L922.598 239.982C927.075 241.086 929.314 243.34 929.314 246.744ZM945.607 222.686C945.607 223.514 945.315 224.219 944.733 224.802C944.15 225.385 943.445 225.676 942.617 225.676C941.789 225.676 941.083 225.385 940.501 224.802C939.918 224.219 939.627 223.514 939.627 222.686C939.627 221.858 939.918 221.153 940.501 220.57C941.083 219.987 941.789 219.696 942.617 219.696C943.445 219.696 944.15 219.987 944.733 220.57C945.315 221.153 945.607 221.858 945.607 222.686ZM944.733 230.46V253H940.501V230.46H944.733ZM974.85 246.744C974.85 248.707 973.992 250.363 972.274 251.712C970.557 253.061 968.395 253.736 965.788 253.736C963.519 253.736 961.526 253.153 959.808 251.988C958.091 250.792 956.864 249.228 956.128 247.296L959.9 245.686C960.452 247.035 961.25 248.093 962.292 248.86C963.366 249.596 964.531 249.964 965.788 249.964C967.138 249.964 968.257 249.673 969.146 249.09C970.066 248.507 970.526 247.817 970.526 247.02C970.526 245.579 969.422 244.521 967.214 243.846L963.35 242.88C958.965 241.776 956.772 239.66 956.772 236.532C956.772 234.477 957.6 232.837 959.256 231.61C960.943 230.353 963.09 229.724 965.696 229.724C967.69 229.724 969.484 230.199 971.078 231.15C972.704 232.101 973.838 233.373 974.482 234.968L970.71 236.532C970.281 235.581 969.576 234.845 968.594 234.324C967.644 233.772 966.57 233.496 965.374 233.496C964.27 233.496 963.274 233.772 962.384 234.324C961.526 234.876 961.096 235.551 961.096 236.348C961.096 237.636 962.308 238.556 964.73 239.108L968.134 239.982C972.612 241.086 974.85 243.34 974.85 246.744ZM994.593 253.368C992.753 253.368 991.22 252.801 989.993 251.666C988.797 250.531 988.184 248.952 988.153 246.928V234.324H984.197V230.46H988.153V223.56H992.385V230.46H997.905V234.324H992.385V245.548C992.385 247.051 992.676 248.078 993.259 248.63C993.842 249.151 994.501 249.412 995.237 249.412C995.574 249.412 995.896 249.381 996.203 249.32C996.54 249.228 996.847 249.121 997.123 248.998L998.457 252.77C997.353 253.169 996.065 253.368 994.593 253.368ZM1011.92 246.1C1011.92 247.204 1012.38 248.124 1013.3 248.86C1014.25 249.596 1015.36 249.964 1016.62 249.964C1018.39 249.964 1019.97 249.305 1021.35 247.986C1022.76 246.667 1023.47 245.119 1023.47 243.34C1022.15 242.297 1020.31 241.776 1017.95 241.776C1016.23 241.776 1014.79 242.19 1013.63 243.018C1012.49 243.846 1011.92 244.873 1011.92 246.1ZM1017.4 229.724C1020.53 229.724 1022.99 230.567 1024.8 232.254C1026.61 233.91 1027.52 236.195 1027.52 239.108V253H1023.47V249.872H1023.29C1021.54 252.448 1019.21 253.736 1016.29 253.736C1013.81 253.736 1011.72 253 1010.04 251.528C1008.38 250.056 1007.55 248.216 1007.55 246.008C1007.55 243.677 1008.43 241.822 1010.18 240.442C1011.95 239.062 1014.32 238.372 1017.26 238.372C1019.77 238.372 1021.84 238.832 1023.47 239.752V238.786C1023.47 237.314 1022.89 236.072 1021.72 235.06C1020.56 234.017 1019.19 233.496 1017.63 233.496C1015.27 233.496 1013.4 234.493 1012.02 236.486L1008.29 234.14C1010.34 231.196 1013.38 229.724 1017.4 229.724ZM1039.65 230.46H1043.7V233.588H1043.88C1044.53 232.484 1045.51 231.564 1046.83 230.828C1048.18 230.092 1049.57 229.724 1051.01 229.724C1053.77 229.724 1055.89 230.521 1057.36 232.116C1058.86 233.68 1059.61 235.919 1059.61 238.832V253H1055.38V239.108C1055.29 235.428 1053.44 233.588 1049.82 233.588C1048.13 233.588 1046.72 234.278 1045.58 235.658C1044.45 237.007 1043.88 238.633 1043.88 240.534V253H1039.65V230.46ZM1082.25 253.736C1078.9 253.736 1076.13 252.601 1073.92 250.332C1071.74 248.001 1070.65 245.134 1070.65 241.73C1070.65 238.265 1071.74 235.397 1073.92 233.128C1076.13 230.859 1078.9 229.724 1082.25 229.724C1084.55 229.724 1086.56 230.307 1088.27 231.472C1089.99 232.607 1091.28 234.186 1092.14 236.21L1088.27 237.82C1087.08 234.999 1084.98 233.588 1081.97 233.588C1080.04 233.588 1078.37 234.37 1076.96 235.934C1075.58 237.498 1074.89 239.43 1074.89 241.73C1074.89 244.03 1075.58 245.962 1076.96 247.526C1078.37 249.09 1080.04 249.872 1081.97 249.872C1085.07 249.872 1087.25 248.461 1088.5 245.64L1092.27 247.25C1091.45 249.274 1090.14 250.869 1088.36 252.034C1086.62 253.169 1084.58 253.736 1082.25 253.736ZM1113.23 253.736C1109.92 253.736 1107.19 252.601 1105.04 250.332C1102.9 248.063 1101.82 245.195 1101.82 241.73C1101.82 238.295 1102.87 235.443 1104.95 233.174C1107.04 230.874 1109.7 229.724 1112.96 229.724C1116.3 229.724 1118.95 230.813 1120.91 232.99C1122.91 235.137 1123.9 238.157 1123.9 242.052L1123.86 242.512H1106.15C1106.21 244.72 1106.94 246.499 1108.36 247.848C1109.77 249.197 1111.45 249.872 1113.42 249.872C1116.11 249.872 1118.23 248.523 1119.76 245.824L1123.54 247.664C1122.52 249.565 1121.11 251.053 1119.3 252.126C1117.52 253.199 1115.5 253.736 1113.23 253.736ZM1106.47 239.016H1119.4C1119.27 237.452 1118.63 236.164 1117.46 235.152C1116.33 234.109 1114.8 233.588 1112.86 233.588C1111.27 233.588 1109.89 234.079 1108.72 235.06C1107.59 236.041 1106.84 237.36 1106.47 239.016ZM1157.57 253H1153.34V220.064H1157.57V253ZM1170.83 230.46H1174.88V233.588H1175.06C1175.71 232.484 1176.69 231.564 1178.01 230.828C1179.36 230.092 1180.75 229.724 1182.19 229.724C1184.95 229.724 1187.07 230.521 1188.54 232.116C1190.04 233.68 1190.8 235.919 1190.8 238.832V253H1186.56V239.108C1186.47 235.428 1184.62 233.588 1181 233.588C1179.31 233.588 1177.9 234.278 1176.77 235.658C1175.63 237.007 1175.06 238.633 1175.06 240.534V253H1170.83V230.46ZM1220.15 246.744C1220.15 248.707 1219.29 250.363 1217.57 251.712C1215.86 253.061 1213.69 253.736 1211.09 253.736C1208.82 253.736 1206.82 253.153 1205.11 251.988C1203.39 250.792 1202.16 249.228 1201.43 247.296L1205.2 245.686C1205.75 247.035 1206.55 248.093 1207.59 248.86C1208.66 249.596 1209.83 249.964 1211.09 249.964C1212.44 249.964 1213.56 249.673 1214.44 249.09C1215.36 248.507 1215.82 247.817 1215.82 247.02C1215.82 245.579 1214.72 244.521 1212.51 243.846L1208.65 242.88C1204.26 241.776 1202.07 239.66 1202.07 236.532C1202.07 234.477 1202.9 232.837 1204.55 231.61C1206.24 230.353 1208.39 229.724 1210.99 229.724C1212.99 229.724 1214.78 230.199 1216.38 231.15C1218 232.101 1219.14 233.373 1219.78 234.968L1216.01 236.532C1215.58 235.581 1214.87 234.845 1213.89 234.324C1212.94 233.772 1211.87 233.496 1210.67 233.496C1209.57 233.496 1208.57 233.772 1207.68 234.324C1206.82 234.876 1206.39 235.551 1206.39 236.348C1206.39 237.636 1207.61 238.556 1210.03 239.108L1213.43 239.982C1217.91 241.086 1220.15 243.34 1220.15 246.744ZM1236.44 222.686C1236.44 223.514 1236.15 224.219 1235.57 224.802C1234.99 225.385 1234.28 225.676 1233.45 225.676C1232.62 225.676 1231.92 225.385 1231.34 224.802C1230.75 224.219 1230.46 223.514 1230.46 222.686C1230.46 221.858 1230.75 221.153 1231.34 220.57C1231.92 219.987 1232.62 219.696 1233.45 219.696C1234.28 219.696 1234.99 219.987 1235.57 220.57C1236.15 221.153 1236.44 221.858 1236.44 222.686ZM1235.57 230.46V253H1231.34V230.46H1235.57ZM1258.33 249.872C1260.42 249.872 1262.12 249.121 1263.44 247.618C1264.82 246.115 1265.51 244.153 1265.51 241.73C1265.51 239.369 1264.82 237.421 1263.44 235.888C1262.09 234.355 1260.39 233.588 1258.33 233.588C1256.31 233.588 1254.6 234.355 1253.22 235.888C1251.84 237.421 1251.15 239.369 1251.15 241.73C1251.15 244.122 1251.84 246.069 1253.22 247.572C1254.6 249.105 1256.31 249.872 1258.33 249.872ZM1258.19 263.672C1256.94 263.672 1255.75 263.503 1254.65 263.166C1253.55 262.859 1252.53 262.415 1251.61 261.832C1250.73 261.249 1249.96 260.559 1249.31 259.762C1248.67 258.965 1248.18 258.075 1247.84 257.094L1251.84 255.438C1252.3 256.757 1253.1 257.815 1254.24 258.612C1255.37 259.409 1256.69 259.808 1258.19 259.808C1260.49 259.808 1262.29 259.118 1263.57 257.738C1264.86 256.358 1265.51 254.457 1265.51 252.034V249.872H1265.32C1264.53 251.068 1263.44 252.019 1262.06 252.724C1260.71 253.399 1259.24 253.736 1257.64 253.736C1254.7 253.736 1252.17 252.586 1250.05 250.286C1247.97 247.925 1246.92 245.073 1246.92 241.73C1246.92 238.387 1247.97 235.551 1250.05 233.22C1252.17 230.889 1254.7 229.724 1257.64 229.724C1259.24 229.724 1260.71 230.077 1262.06 230.782C1263.44 231.457 1264.53 232.392 1265.32 233.588H1265.51V230.46H1269.55V252.034C1269.55 255.653 1268.53 258.489 1266.47 260.544C1264.39 262.629 1261.63 263.672 1258.19 263.672ZM1282.07 220.064H1286.31V230.46L1286.12 233.588H1286.31C1286.95 232.484 1287.93 231.564 1289.25 230.828C1290.6 230.092 1292 229.724 1293.44 229.724C1296.2 229.724 1298.31 230.521 1299.78 232.116C1301.29 233.68 1302.04 235.919 1302.04 238.832V253H1297.81V239.66C1297.81 235.612 1296.01 233.588 1292.42 233.588C1290.71 233.588 1289.25 234.309 1288.05 235.75C1286.89 237.161 1286.31 238.817 1286.31 240.718V253H1282.07V220.064ZM1322.12 253.368C1320.28 253.368 1318.75 252.801 1317.52 251.666C1316.33 250.531 1315.71 248.952 1315.68 246.928V234.324H1311.73V230.46H1315.68V223.56H1319.91V230.46H1325.43V234.324H1319.91V245.548C1319.91 247.051 1320.21 248.078 1320.79 248.63C1321.37 249.151 1322.03 249.412 1322.77 249.412C1323.1 249.412 1323.43 249.381 1323.73 249.32C1324.07 249.228 1324.38 249.121 1324.65 248.998L1325.99 252.77C1324.88 253.169 1323.59 253.368 1322.12 253.368ZM1364.41 224.112V253H1360.17V224.112H1350.97V220.064H1373.61V224.112H1364.41ZM1386.14 253H1381.91V230.46H1385.96V234.14H1386.14C1386.57 232.944 1387.44 231.932 1388.76 231.104C1390.11 230.245 1391.43 229.816 1392.72 229.816C1393.94 229.816 1394.99 230 1395.85 230.368L1394.56 234.462C1394.04 234.247 1393.21 234.14 1392.07 234.14C1390.48 234.14 1389.08 234.784 1387.89 236.072C1386.72 237.36 1386.14 238.863 1386.14 240.58V253ZM1408.16 246.1C1408.16 247.204 1408.62 248.124 1409.54 248.86C1410.49 249.596 1411.6 249.964 1412.85 249.964C1414.63 249.964 1416.21 249.305 1417.59 247.986C1419 246.667 1419.71 245.119 1419.71 243.34C1418.39 242.297 1416.55 241.776 1414.19 241.776C1412.47 241.776 1411.03 242.19 1409.86 243.018C1408.73 243.846 1408.16 244.873 1408.16 246.1ZM1413.64 229.724C1416.76 229.724 1419.23 230.567 1421.04 232.254C1422.85 233.91 1423.76 236.195 1423.76 239.108V253H1419.71V249.872H1419.52C1417.78 252.448 1415.44 253.736 1412.53 253.736C1410.05 253.736 1407.96 253 1406.28 251.528C1404.62 250.056 1403.79 248.216 1403.79 246.008C1403.79 243.677 1404.67 241.822 1406.41 240.442C1408.19 239.062 1410.55 238.372 1413.5 238.372C1416.01 238.372 1418.08 238.832 1419.71 239.752V238.786C1419.71 237.314 1419.12 236.072 1417.96 235.06C1416.79 234.017 1415.43 233.496 1413.87 233.496C1411.5 233.496 1409.63 234.493 1408.25 236.486L1404.53 234.14C1406.58 231.196 1409.62 229.724 1413.64 229.724ZM1445.97 253.736C1442.63 253.736 1439.85 252.601 1437.64 250.332C1435.46 248.001 1434.38 245.134 1434.38 241.73C1434.38 238.265 1435.46 235.397 1437.64 233.128C1439.85 230.859 1442.63 229.724 1445.97 229.724C1448.27 229.724 1450.28 230.307 1451.99 231.472C1453.71 232.607 1455 234.186 1455.86 236.21L1451.99 237.82C1450.8 234.999 1448.7 233.588 1445.69 233.588C1443.76 233.588 1442.09 234.37 1440.68 235.934C1439.3 237.498 1438.61 239.43 1438.61 241.73C1438.61 244.03 1439.3 245.962 1440.68 247.526C1442.09 249.09 1443.76 249.872 1445.69 249.872C1448.79 249.872 1450.97 248.461 1452.22 245.64L1456 247.25C1455.17 249.274 1453.86 250.869 1452.09 252.034C1450.34 253.169 1448.3 253.736 1445.97 253.736ZM1486.88 253H1481.78L1474.74 242.374L1471.29 245.778V253H1467.06V220.064H1471.29V240.35L1481.04 230.46H1486.47V230.644L1477.68 239.384L1486.88 252.816V253ZM1506.1 253.736C1502.79 253.736 1500.06 252.601 1497.91 250.332C1495.77 248.063 1494.69 245.195 1494.69 241.73C1494.69 238.295 1495.73 235.443 1497.82 233.174C1499.91 230.874 1502.57 229.724 1505.82 229.724C1509.17 229.724 1511.82 230.813 1513.78 232.99C1515.78 235.137 1516.77 238.157 1516.77 242.052L1516.73 242.512H1499.02C1499.08 244.72 1499.81 246.499 1501.22 247.848C1502.63 249.197 1504.32 249.872 1506.28 249.872C1508.98 249.872 1511.1 248.523 1512.63 245.824L1516.4 247.664C1515.39 249.565 1513.98 251.053 1512.17 252.126C1510.39 253.199 1508.37 253.736 1506.1 253.736ZM1499.34 239.016H1512.26C1512.14 237.452 1511.5 236.164 1510.33 235.152C1509.2 234.109 1507.66 233.588 1505.73 233.588C1504.14 233.588 1502.76 234.079 1501.59 235.06C1500.46 236.041 1499.71 237.36 1499.34 239.016ZM1532.23 253H1528V230.46H1532.05V234.14H1532.23C1532.66 232.944 1533.54 231.932 1534.86 231.104C1536.21 230.245 1537.52 229.816 1538.81 229.816C1540.04 229.816 1541.08 230 1541.94 230.368L1540.65 234.462C1540.13 234.247 1539.3 234.14 1538.17 234.14C1536.57 234.14 1535.18 234.784 1533.98 236.072C1532.82 237.36 1532.23 238.863 1532.23 240.58V253Z" fill="black"/>
<path d="M60.0657 162.624C59.3642 164 58.5283 165.64 56.0038 170.592C46.4176 165.476 42.1292 155.014 46.1717 147.084C50.2142 139.154 61.2105 136.456 70.9969 141.179C68.2957 146.477 67.6017 147.839 66.7307 149.548C66.0714 150.843 65.3107 152.336 63.5009 155.886C61.4937 159.823 60.8619 161.063 60.1927 162.375L60.0657 162.624Z" fill="#1D00FA" stroke="#1D00FA"/>
<path d="M66.3098 148.823C67.0112 147.447 67.8472 145.808 70.3717 140.855C79.9579 145.972 84.2463 156.433 80.2038 164.363C76.1613 172.293 65.165 174.991 55.3786 170.268C58.0798 164.97 58.7738 163.608 59.6447 161.899C60.3041 160.605 61.0648 159.112 62.8746 155.561C64.8818 151.624 65.5136 150.385 66.1828 149.072L66.3098 148.823Z" fill="#C5E4FF" stroke="#1D00FA"/>
<path d="M197.011 57.9251C195.601 57.1443 193.919 56.2136 188.833 53.3986C194.524 43.6077 205.613 39.5219 213.753 44.0269C221.893 48.5318 224.295 60.0843 218.991 70.0894C213.55 67.0774 212.154 66.3051 210.402 65.3356C209.076 64.6025 207.547 63.7567 203.912 61.7445C199.88 59.5129 198.611 58.8104 197.267 58.0664L197.011 57.9251Z" fill="#FA0000" stroke="#FA0000"/>
<path d="M211.188 64.8874C212.598 65.6682 214.28 66.5989 219.366 69.4139C213.675 79.2048 202.586 83.2906 194.446 78.7856C186.306 74.2807 183.904 62.7282 189.208 52.7231C194.649 55.7351 196.045 56.5074 197.798 57.4769C199.123 58.21 200.652 59.0558 204.287 61.068C208.32 63.2996 209.589 64.0021 210.933 64.7461L211.188 64.8874Z" fill="#FFCECE" stroke="#FA0000"/>
<path d="M215.173 258.697C224.811 253.451 227.511 239.84 221.205 228.295C208.989 234.944 213.392 232.547 203.754 237.793C194.116 243.039 197.647 241.119 186.303 247.292C192.61 258.836 205.535 263.942 215.173 258.697Z" fill="#FA7D00"/>
<path d="M196.709 243.323C195.118 244.189 193.221 245.222 187.46 248.357C181.551 237.077 184.325 224.084 193.529 219.074C202.733 214.065 215.177 218.775 221.476 229.843C215.313 233.196 213.74 234.053 211.764 235.128C210.275 235.94 208.556 236.875 204.468 239.1C199.935 241.568 198.508 242.344 196.997 243.167L196.709 243.323Z" fill="#FFE5CB" stroke="#FA7D00"/>
<path d="M240.149 122.857C233.99 122.879 228.011 125.331 223.148 129.829C218.286 134.328 214.815 140.618 213.28 147.714H183.444C182.458 143.042 180.62 138.684 178.06 134.95C175.501 131.217 172.283 128.198 168.634 126.109C164.985 124.019 160.995 122.91 156.945 122.859C152.896 122.808 148.887 123.818 145.202 125.815L123.075 92.9209C126.716 87.2352 128.697 80.2906 128.717 73.1429C128.717 66.5878 127.083 60.18 124.022 54.7297C120.961 49.2794 116.61 45.0314 111.519 42.5229C106.429 40.0144 100.828 39.358 95.4236 40.6368C90.0196 41.9157 85.0558 45.0722 81.1597 49.7073C77.2637 54.3424 74.6105 60.2479 73.5355 66.677C72.4606 73.1061 73.0123 79.77 75.1208 85.8261C77.2294 91.8821 80.8 97.0584 85.3813 100.7C89.9625 104.342 95.3486 106.286 100.858 106.286C104.785 106.265 108.663 105.257 112.239 103.328L134.358 136.222C130.702 141.898 128.72 148.849 128.72 156C128.72 163.151 130.702 170.102 134.358 175.778L112.239 208.672C108.663 206.743 104.785 205.735 100.858 205.714C95.3486 205.714 89.9625 207.658 85.3813 211.3C80.8 214.942 77.2294 220.118 75.1208 226.174C73.0123 232.23 72.4606 238.894 73.5355 245.323C74.6105 251.752 77.2637 257.658 81.1597 262.293C85.0558 266.928 90.0196 270.084 95.4236 271.363C100.828 272.642 106.429 271.986 111.519 269.477C116.61 266.969 120.961 262.721 124.022 257.27C127.083 251.82 128.717 245.412 128.717 238.857C128.697 231.709 126.716 224.765 123.075 219.079L145.195 186.185C148.88 188.184 152.89 189.194 156.94 189.144C160.99 189.094 164.982 187.985 168.632 185.896C172.281 183.806 175.5 180.787 178.06 177.053C180.62 173.318 182.458 168.959 183.444 164.286H213.28C214.592 170.273 217.288 175.702 221.063 179.958C224.838 184.213 229.54 187.124 234.635 188.36C239.731 189.596 245.016 189.107 249.89 186.949C254.763 184.792 259.031 181.051 262.208 176.153C265.385 171.255 267.344 165.395 267.862 159.239C268.38 153.083 267.437 146.877 265.14 141.327C262.842 135.776 259.283 131.103 254.866 127.838C250.448 124.574 245.35 122.848 240.149 122.857ZM86.9294 73.1429C86.9294 69.8653 87.7463 66.6614 89.2768 63.9363C90.8074 61.2111 92.9828 59.0871 95.528 57.8329C98.0732 56.5786 100.874 56.2504 103.576 56.8899C106.278 57.5293 108.76 59.1075 110.708 61.4251C112.656 63.7427 113.982 66.6954 114.52 69.9099C115.057 73.1245 114.782 76.4564 113.727 79.4845C112.673 82.5125 110.888 85.1006 108.597 86.9215C106.306 88.7424 103.613 89.7143 100.858 89.7143C97.1642 89.7143 93.6213 87.9684 91.0091 84.8606C88.3969 81.7529 86.9294 77.5379 86.9294 73.1429ZM100.858 255.429C98.1035 255.429 95.4105 254.457 93.1199 252.636C90.8292 250.815 89.0439 248.227 87.9896 245.199C86.9354 242.171 86.6595 238.839 87.197 235.624C87.7345 232.41 89.0611 229.457 91.0091 227.139C92.9571 224.822 95.439 223.244 98.141 222.604C100.843 221.965 103.644 222.293 106.189 223.547C108.734 224.801 110.91 226.925 112.44 229.651C113.971 232.376 114.788 235.58 114.788 238.857C114.788 243.252 113.32 247.467 110.708 250.575C108.096 253.683 104.553 255.429 100.858 255.429ZM156.575 172.571C153.82 172.571 151.127 171.6 148.836 169.779C146.546 167.958 144.76 165.37 143.706 162.342C142.652 159.314 142.376 155.982 142.913 152.767C143.451 149.553 144.777 146.6 146.725 144.282C148.674 141.965 151.155 140.386 153.857 139.747C156.559 139.108 159.36 139.436 161.905 140.69C164.45 141.944 166.626 144.068 168.156 146.793C169.687 149.519 170.504 152.722 170.504 156C170.504 160.395 169.036 164.61 166.424 167.718C163.812 170.826 160.269 172.571 156.575 172.571ZM240.149 172.571C237.395 172.571 234.701 171.6 232.411 169.779C230.12 167.958 228.335 165.37 227.281 162.342C226.226 159.314 225.951 155.982 226.488 152.767C227.025 149.553 228.352 146.6 230.3 144.282C232.248 141.965 234.73 140.386 237.432 139.747C240.134 139.108 242.935 139.436 245.48 140.69C248.025 141.944 250.201 144.068 251.731 146.793C253.262 149.519 254.079 152.722 254.079 156C254.079 160.395 252.611 164.61 249.999 167.718C247.387 170.826 243.844 172.571 240.149 172.571Z" fill="#169400"/>
<path d="M310.256 148.343H296.088V38.0788H310.256L348.602 105.223H349.218L387.564 38.0788H401.732V148.343H387.564V82.8928L388.18 64.4128H387.564L353.068 124.935H344.752L310.256 64.4128H309.64L310.256 82.8928V148.343ZM512.932 38.0788V51.6308H462.728V86.5888H508.004V99.8328H462.728V134.791H512.932V148.343H448.56V38.0788H512.932ZM570.835 51.6308V90.4388H593.627C599.376 90.4388 604.253 88.5908 608.257 84.8948C612.261 81.0961 614.263 76.4248 614.263 70.8808C614.263 65.7474 612.363 61.2814 608.565 57.4828C604.869 53.5814 600.197 51.6308 594.551 51.6308H570.835ZM570.835 148.343H556.667V38.0788H594.243C603.791 38.0788 611.901 41.2614 618.575 47.6268C625.351 53.8894 628.739 61.6408 628.739 70.8808C628.739 78.4781 626.223 85.2541 621.193 91.2088C616.265 97.0608 610.002 100.808 602.405 102.451L602.097 102.913L633.051 147.727V148.343H616.265L586.543 103.683H570.835V148.343Z" fill="black"/>
<path d="M797.664 57.1376V153.85H783.496V57.1376H752.696V43.5856H828.464V57.1376H797.664Z" fill="black"/>
<path d="M670.284 131.21L669.001 60.0021C668.934 56.2623 669.67 52.5712 671.168 49.1397C672.665 45.7081 674.894 42.6032 677.728 40.0024C680.562 37.4015 683.944 35.3555 687.683 33.9812C691.422 32.607 695.443 31.9313 699.518 31.9929C703.593 32.0545 707.641 32.8521 711.431 34.3402C715.221 35.8282 718.679 37.9776 721.608 40.6656C724.536 43.3536 726.878 46.5275 728.499 50.0062C730.121 53.4849 730.99 57.2003 731.057 60.9401L732.339 132.128C732.408 135.868 731.674 139.56 730.178 142.992C728.682 146.425 726.455 149.531 723.622 152.133C720.789 154.736 717.407 156.783 713.669 158.159C709.93 159.535 705.909 160.212 701.834 160.152C697.759 160.092 693.71 159.296 689.919 157.81C686.128 156.323 682.669 154.175 679.739 151.488C676.808 148.801 674.465 145.627 672.842 142.149C671.219 138.671 670.353 134.95 670.284 131.21ZM723.824 89.9604L723.301 60.8329C723.275 58.0139 722.641 55.2092 721.436 52.5805C720.231 49.9518 718.478 47.5511 716.278 45.5169C714.079 43.4827 711.477 41.8552 708.621 40.7284C705.766 39.6016 702.715 38.9978 699.643 38.9517C696.571 38.9056 693.54 39.4182 690.724 40.4599C687.908 41.5015 685.363 43.0517 683.236 45.021C681.109 46.9903 679.441 49.3396 678.33 51.9336C677.22 54.5276 676.687 57.3148 676.763 60.1345L677.285 89.262L723.824 89.9604Z" fill="#008029"/>
<path d="M693.887 62.66C693.887 63.9667 693.42 65.0867 692.487 66.02C691.6 66.9533 690.48 67.42 689.127 67.42C687.82 67.42 686.7 66.9533 685.767 66.02C684.834 65.0867 684.367 63.9667 684.367 62.66C684.367 61.3067 684.834 60.1867 685.767 59.3C686.7 58.3667 687.82 57.9 689.127 57.9C690.48 57.9 691.6 58.3667 692.487 59.3C693.42 60.1867 693.887 61.3067 693.887 62.66Z" fill="black"/>
<path d="M713.887 62.66C713.887 63.9667 713.42 65.0867 712.487 66.02C711.6 66.9533 710.48 67.42 709.127 67.42C707.82 67.42 706.7 66.9533 705.767 66.02C704.834 65.0867 704.367 63.9667 704.367 62.66C704.367 61.3067 704.834 60.1867 705.767 59.3C706.7 58.3667 707.82 57.9 709.127 57.9C710.48 57.9 711.6 58.3667 712.487 59.3C713.42 60.1867 713.887 61.3067 713.887 62.66Z" fill="black"/>
<path d="M713.007 68.8369C713.007 80.7687 689.007 87.1935 689.007 73.4252" stroke="black" stroke-width="5"/>
</svg>
    </div>
    <div class="menu">
        <a href="https://merit-sastra.streamlit.app/">Home</a>
        <a href="https://merit-dashboard.streamlit.app/" target="_blank">Dataset</a>
        <a href="https://merit-mining.streamlit.app/" target="_blank">Association Mining</a>
        <a href="https://mining-query.streamlit.app/" target="_blank">Track MDR</a>
        <a href="https://merit-dataset.streamlit.app/" target="_blank">Antimicrobial Trend</a>
        <a href="https://merit-aboutus.streamlit.app/">About Us</a>
    </div>
</nav>


<div class="content">
'''

# Injecting the navigation bar and content padding into the Streamlit app
st.markdown(navbar_html, unsafe_allow_html=True)

a,b = st.columns([0.3,0.7])

# with st.spinner("Fetching Datasets..."):
#     import getresource as gr
#     import os
#     gdrive_link = "https://drive.google.com/uc?id=1mgKajVm3IpFw2a52d_j5VXz5v0K0F9sX"  # Replace with the actual file ID
#     folder_name = "resource"
#     download_path = "./downloads"  # Path to store the zip file
#     extract_path = "./resource/resource"  # Path to extract the folder
#     gr.download_and_extract_with_gdown(gdrive_link, folder_name, download_path, extract_path)
# with b:
#     st.write(os.listdir("./resource/resource/Final Data/Ecoli data"))

with a:
    with st.container(border=True):
        
        st.subheader("Available Plots")
        st.write("---")
        with st.expander("% of Resistance over Age Group"):
            org = st.selectbox("Choose Organism",["Not Chosen","Acinetobacter baumannii", "Enterobacter spp",
            "Escherichia coli", "Enterococcus faecium", "Klebsiella pneumoniae",
            "Pseudomonas aeruginosa", "Staphylococcus aureus"
            ],key=1)
            import chisquare as c
            con = "India"
            try:
                con = st.selectbox("Choose Country",c.get_cons(org))
            except:
                pass
            if st.button("Display Plot",key=12):
                import chisquare as c
                fig= c.plot_age_group(org,con)
        
                with b:
                    st.subheader(f"% of Resistance Over the Years - Country: {con}")
                    st.plotly_chart(fig)
        with st.expander("% of Resistance over Country"):
            org = st.selectbox("Choose Organism",["Not Chosen","Acinetobacter baumannii", "Enterobacter spp",
            "Escherichia coli", "Enterococcus faecium", "Klebsiella pneumoniae",
            "Pseudomonas aeruginosa", "Staphylococcus aureus"
            ],key=2)
            import chisquare as c
            con = "India"
            try:
                con = st.selectbox("Choose Country",c.get_cons(org))
            except:
                pass
            if st.button("Display Plot",key=99):
                with b:
                    fig,dfff = c.plot_country_group(org,con)
                    st.plotly_chart(fig)


        with st.expander("Antibiotic Resistant Profile for Organism"):
            org = st.selectbox("Choose Organism",["Not Chosen","Acinetobacter baumannii", "Enterobacter spp",
            "Escherichia coli", "Enterococcus faecium", "Klebsiella pneumoniae",
            "Pseudomonas aeruginosa", "Staphylococcus aureus"
            ],key=3)
            if st.button("Display Plot",key=22):
                import chisquare as c
                with a:
                    fig,dfplotc,fig1=c.plot_antibiotic_resistance(org)
                    with b:
                        st.plotly_chart(fig)
                        st.plotly_chart(fig1)
        
        with st.expander("Country Wise Resistant Profile"):
            org = st.selectbox("Choose Organism",["Not Chosen","Acinetobacter baumannii", "Enterobacter spp",
            "Escherichia coli", "Enterococcus faecium", "Klebsiella pneumoniae",
            "Pseudomonas aeruginosa", "Staphylococcus aureus"
            ],key=4)
            if st.button("Display Plot",key=23):
                import chisquare as c
                with a:
                    fig=c.conplot_geo(org)
                    with b:
                        st.plotly_chart(fig)
    

            
