import numpy as np
import matplotlib.pyplot as plt

# movielens10m data
# collrank method on illidan server
# lambda = 7000, rank = 100
# iteration, training time (sec), objective function, pairwise error, ndcg@10
c_4t = [
[0, 0.197260, 285183632.851423, 0.384060, 0.301689],
[1, 148.860754, 163123186.458265, 0.224951, 0.592250],
[2, 286.272239, 159969343.118798, 0.218510, 0.626391],
[3, 428.945712, 153657969.928672, 0.201548, 0.667498],
[4, 569.552939, 150822639.924113, 0.193795, 0.685022],
[5, 710.473846, 149718882.841498, 0.191519, 0.689996],
[6, 848.863479, 149247389.673486, 0.191014, 0.691900],
[7, 988.889957, 149020920.047827, 0.190853, 0.692587],
[8, 1127.855999, 148897040.636256, 0.190779, 0.693310]
]

c_8t = [
[0, 0.197323, 284942326.405430, 0.377036, 0.321790],
[1, 86.383598, 163110439.358476, 0.224962, 0.592233],
[2, 171.003080, 159740894.784202, 0.217867, 0.626433],
[3, 257.022530, 153707663.892757, 0.201621, 0.668030],
[4, 340.212255, 150818069.307056, 0.193752, 0.685155],
[5, 423.439858, 149700876.469415, 0.191522, 0.690172],
[6, 507.313156, 149234503.737330, 0.190965, 0.691791],
[7, 590.516661, 149012712.115544, 0.190770, 0.692340],
[8, 670.591445, 148892359.927056, 0.190719, 0.692665],
[9, 753.960838, 148819787.610987, 0.190671, 0.693020],
[10, 838.933727, 148772752.478132, 0.190640, 0.693271],
[11, 925.793559, 148740711.614995, 0.190641, 0.693264],
[12, 1009.983366, 148718111.644305, 0.190642, 0.693352],
[13, 1094.450964, 148701772.389786, 0.190633, 0.693295],
[14, 1180.894977, 148689648.490627, 0.190623, 0.693395],
[15, 1268.612580, 148680408.317502, 0.190615, 0.693415],
[16, 1355.399083, 148673165.551754, 0.190636, 0.693344],
[17, 1441.920139, 148667324.835175, 0.190637, 0.693551],
[18, 1526.856687, 148662537.410281, 0.190642, 0.693476],
[19, 1610.366814, 148658533.001738, 0.190645, 0.693512],
[20, 1696.756396, 148655126.167640, 0.190647, 0.693465]
]

# our method
w_1c = [
[0, 0.0, 4.706734166031446e8, 0.379201590651579, 0.31671894620514973],
[1, 55.147901636, 1.8907217190919593e8, 0.26053857399581276, 0.5695933369677866],
[2, 161.01776465400002, 1.5322058956319854e8, 0.20421301978002718, 0.6661524911199446],
[3, 271.138540724, 1.501932813890491e8, 0.19507469155295318, 0.6833893031643736],
[4, 381.659124077, 1.494384142376757e8, 0.19248749416331884, 0.6886703792607922],
[5, 492.895469536, 1.4913995821275786e8, 0.19151172439152037, 0.6907597805861468],
[6, 605.483878824, 1.4898555983319846e8, 0.19107540642999715, 0.6918099096014705],
[7, 718.572835648, 1.4889335317157072e8, 0.1908399081291831, 0.6926235974743318],
[8, 827.063726799, 1.488333827943364e8, 0.1907536510300872, 0.6929313958547338],
[9, 933.999315934, 1.487919789236598e8, 0.19068869622181545, 0.6930374715388257],
[10, 1041.7065243, 1.4876204809945062e8, 0.19065262338892994, 0.6931730481856057],
[11, 1150.87423036, 1.4873961234785748e8, 0.19061708166602312, 0.6933523750484415],
[12, 1253.952510281, 1.4872230754344136e8, 0.19062827785268263, 0.6933129932495025],
[13, 1357.135527347, 1.487086544241098e8, 0.1906292739358572, 0.6933633834394226],
[14, 1460.2812413210002, 1.486976830909762e8, 0.19060352616006132, 0.6936885358330724],
[15, 1563.3756456840001, 1.486887308284452e8, 0.1905906952124241, 0.6936867243424805],
[16, 1666.474392798, 1.4868132899711356e8, 0.1905813949036421, 0.693661674959574],
[17, 1769.4935141400001, 1.486751371042081e8, 0.19057784055187793, 0.6936002517498102],
[18, 1872.6644807880002, 1.4866990257512668e8, 0.19060034407881768, 0.6934435385059109],
[19, 1976.0004763140003, 1.4866543496517974e8, 0.19058588331979526, 0.693485114478745],
[20, 2079.1802887080003, 1.4866158874787158e8, 0.1905783360934541, 0.6933678144932507]
]

# Avoid |Omega| complexity by exploiting training data only has rating
w2_1c = [
[0, 0.0, 4.706734166032546e8, 0.379201590651579, 0.31671894620514973],
[1, 41.865658362, 1.89072171909196e8, 0.26053857399581276, 0.5695933369677866],
[2, 115.73924114900001, 1.5322058956319863e8, 0.20421301978002718, 0.6661524911199446],
[3, 189.020125876, 1.5019328138904914e8, 0.19507469155295318, 0.6833893031643736],
[4, 258.168910772, 1.494384142376757e8, 0.19248749416331884, 0.6886703792607922],
[5, 327.101576706, 1.4913995821275792e8, 0.19151172439152037, 0.6907597805861468],
[6, 394.580958827, 1.4898555983319852e8, 0.19107540642999715, 0.6918099096014705],
[7, 461.640365411, 1.488933531715708e8, 0.1908399081291831, 0.6926235974743318],
[8, 528.710126309, 1.4883338279433653e8, 0.1907536510300872, 0.6929313958547338],
[9, 597.5772372929999, 1.487919789236597e8, 0.19068869622181545, 0.6930374715388257],
[10, 663.2205325479999, 1.4876204809945056e8, 0.19065262336032204, 0.6931730481856057],
[11, 729.407174591, 1.4873961234785753e8, 0.19061708176425868, 0.6933523750484415],
[12, 794.9186097669999, 1.4872230754344139e8, 0.19062827778729685, 0.6933129932495025],
[13, 861.9750589619999, 1.4870865442410976e8, 0.1906292739358572, 0.6933633834394226],
[14, 928.896195778, 1.486976830909762e8, 0.19060352616006132, 0.6936885358330724],
[15, 997.543272352, 1.4868873082844523e8, 0.1905906952124241, 0.6936867243424805],
[16, 1063.536884201, 1.486813289971135e8, 0.1905813949036421, 0.693661674959574],
[17, 1130.022925258, 1.486751371042081e8, 0.19057784055187793, 0.6936002517498102],
[18, 1197.163434417, 1.4866990257512665e8, 0.19060034407881768, 0.6934435385059109],
[19, 1260.002672541, 1.486654349651797e8, 0.19058588331979526, 0.693485114478745],
[20, 1324.975696034, 1.4866158874787146e8, 0.1905783360934541, 0.6933678144932507]
]


w_4c = [
[0, 0.0, 4.70673416603272e8, 0.379201590651579, 0.31671894620514973],
[1, 26.373268084, 1.8907217190919432e8, 0.26053857399581276, 0.5695933369677866],
[2, 74.122111352, 1.5322058956319883e8, 0.20421301978002718, 0.6661524911199446],
[3, 123.027508495, 1.501932813647086e8, 0.19507469285223913, 0.683393019780509],
[4, 172.69476236600002, 1.4943841421850526e8, 0.19248749482826535, 0.6886703792607922],
[5, 222.34905402400003, 1.491399582022699e8, 0.1915117247086326, 0.6907597805861468],
[6, 271.09347739300006, 1.489855598269299e8, 0.19107540634880626, 0.6918099096014705],
[7, 320.1578620270001, 1.4889335316751292e8, 0.19083990753292418, 0.6926235974743318],
[8, 370.73979549500007, 1.488333827915648e8, 0.19075365127882926, 0.6929313958547338],
[9, 419.81870122900006, 1.487919789216749e8, 0.190688697333719, 0.6930374715388257],
[10, 469.2078021930001, 1.4876204809798607e8, 0.1906526231649459, 0.6931730481856057],
[11, 517.725380745, 1.4873961234675428e8, 0.19061708178048237, 0.6933523750484415],
[12, 566.6551476010001, 1.4872230754260218e8, 0.19062827784964562, 0.6933129932495025],
[13, 614.506371315, 1.4870865442347747e8, 0.19062927406916133, 0.6933633834394226],
[14, 664.545779594, 1.4869768309051526e8, 0.19060352704393496, 0.6936885358330724],
[15, 712.745058999, 1.4868873082813057e8, 0.19059069543829152, 0.6936867243424805],
[16, 761.669970068, 1.4868132899692607e8, 0.19058139426687673, 0.693661674959574],
[17, 810.328304142, 1.4867513710413158e8, 0.1905778404779076, 0.6936002517498102],
[18, 859.653686818, 1.4866990257514486e8, 0.1906003440347613, 0.6934435385059109],
[19, 909.197862821, 1.4866543496527684e8, 0.1905858833282812, 0.693485114478745],
[20, 958.812172706, 1.4866158874803627e8, 0.1905783358379797, 0.6933678144932507]
]

w_8c = [
[0, 0.0, 4.7067341660327226e8, 0.379201590651579, 0.31671894620514973],
[1, 21.792929836, 1.8907219219592217e8, 0.2605396655742256, 0.5695879229699836],
[2, 61.59870335, 1.532203193345714e8, 0.2042097259751352, 0.6661689215022298],
[3, 103.47336483699999, 1.5019290205930936e8, 0.19508491175471954, 0.68333734597493],
[4, 145.559607041, 1.494381295705406e8, 0.192498450281434, 0.6887201847736997],
[5, 187.376163338, 1.4913981742903695e8, 0.19151959630351367, 0.690721669902733],
[6, 229.313019997, 1.4898594095570117e8, 0.19107278044832401, 0.6918440599454433],
[7, 271.211557595, 1.4889336322489005e8, 0.19084866547099186, 0.6926200003227936],
[8, 311.697010998, 1.4883336793131027e8, 0.19074568755382265, 0.6929605158167218],
[9, 352.845879879, 1.4879193540621325e8, 0.1906938692431762, 0.6930406281449591],
[10, 395.777545702, 1.4876196673615724e8, 0.1906517695778972, 0.6933018269840094],
[11, 438.690066609, 1.487394874020886e8, 0.19062200389091236, 0.693230401278855],
[12, 481.670351284, 1.4872213708893153e8, 0.19061679250780023, 0.693243262431533],
[13, 524.762179371, 1.4870843961907446e8, 0.19063676694848705, 0.6932543446327835],
[14, 567.154237575, 1.4869742737983468e8, 0.1906091615585618, 0.6935095596529002],
[15, 610.668911231, 1.4868843928407913e8, 0.19058634677611744, 0.6936605834865198],
[16, 653.133008056, 1.4868100774191993e8, 0.19057948885107082, 0.6937392312528239],
[17, 696.351495434, 1.4867479279079953e8, 0.1905786215133218, 0.693667978848665],
[18, 740.632872478, 1.4866954254359877e8, 0.19058792807555655, 0.6934843299077379],
[19, 784.457702869, 1.486650645959837e8, 0.19057857489168833, 0.6935568804104013],
[20, 828.4540681819999, 1.4866121454197448e8, 0.19057370757849934, 0.6934903227638415]
]

c_4t = np.array(c_4t)
c_8t = np.array(c_8t)
w_1c = np.array(w_1c)
w_4c = np.array(w_4c)
w_8c = np.array(w_8c)
w2_1c = np.array(w2_1c)

fig, ax = plt.subplots()
ax.plot(w_1c[:,1], w_1c[:,4], 'r--', label='primal 1 core')
ax.plot(w_4c[:,1], w_4c[:,4], 'k-.', label='primal 4 cores')
ax.plot(w_8c[:,1], w_8c[:,4], 'c', label='primal 8 cores')
#ax.plot(c_1t[:,1], c_1t[:,4], 'm:', label='collrank 1 thread')
ax.plot(c_4t[:,1], c_4t[:,4], 'm-.', label='collrank 4 threads')
ax.plot(c_8t[:,1], c_8t[:,4], 'm', label='collrank 8 threads')
ax.plot(w2_1c[:,1], w_1c[:,4], 'b', label='primal++ 1 core')
ax.set_title('MovieLens10m, 200 ratings/user, rank 100, lambda = 7000')
ax.set_xlabel('Time')
ax.set_ylabel('NDCG')
ax.axis([0, 1000, 0.25, 0.75])
legend = ax.legend(loc='lower right', shadow=True)
frame = legend.get_frame()
frame.set_facecolor('0.90')
plt.show()

fig, ax = plt.subplots()
ax.plot(w_1c[:,1], w_1c[:,3], 'r--', label='primal 1 core')
ax.plot(w_4c[:,1], w_4c[:,3], 'k-.', label='primal 4 cores')
ax.plot(w_8c[:,1], w_8c[:,3], 'c', label='primal 8 cores')
#ax.plot(c_1t[:,1], c_1t[:,3], 'm:', label='collrank 1 thread')
ax.plot(c_4t[:,1], c_4t[:,3], 'm-.', label='collrank 4 threads')
ax.plot(c_8t[:,1], c_8t[:,3], 'm', label='collrank 8 threads')
ax.plot(w2_1c[:,1], w_1c[:,3], 'b', label='primal++ 1 core')
ax.set_title('MovieLens10m, 200 ratings/user, rank 100, lambda = 7000')
ax.set_xlabel('Time')
ax.set_ylabel('Pairwise_Error')
ax.axis([0, 1000, 0.15, 0.4])
legend = ax.legend(loc='upper right', shadow=True)
frame = legend.get_frame()
frame.set_facecolor('0.90')
plt.show()


fig, ax = plt.subplots()
ax.plot(w_1c[:,1], w_1c[:,2], 'r--', label='primal 1 core')
ax.plot(w_4c[:,1], w_4c[:,2], 'k-.', label='primal 4 cores')
ax.plot(w_8c[:,1], w_8c[:,2], 'c', label='primal 8 cores')
#ax.plot(c_1t[:,1], c_1t[:,2], 'm:', label='collrank 1 thread')
ax.plot(c_4t[:,1], c_4t[:,2], 'm-.', label='collrank 4 threads')
ax.plot(c_8t[:,1], c_8t[:,2], 'm', label='collrank 8 threads')
ax.plot(w2_1c[:,1], w_1c[:,2], 'b', label='primal++ 1 core')
ax.set_title('MovieLens10m, 200 ratings/user, rank 100, lambda = 7000')
ax.set_xlabel('Time')
ax.set_ylabel('Objective_Function')
ax.axis([0, 1000, 1.4e8, 5e8])
legend = ax.legend(loc='upper right', shadow=True)
frame = legend.get_frame()
frame.set_facecolor('0.90')
plt.show()


# change lambda to 5000
c_4t = [
[0, 0.195185, 258936003.181592, 0.374941, 0.323591],
[1, 139.046834, 158416668.356924, 0.223534, 0.592738],
[2, 250.633476, 150077285.935234, 0.206824, 0.654420],
[3, 356.305084, 139990569.371472, 0.192745, 0.677800],
[4, 465.114614, 137091746.545778, 0.191563, 0.677477],
[5, 572.149811, 136155328.908169, 0.191559, 0.678642],
[6, 703.981804, 135794613.703583, 0.191504, 0.679535],
[7, 839.058204, 135614509.174054, 0.191384, 0.680023],
[8, 973.479921, 135503503.988665, 0.191312, 0.680516],
[9, 1105.182570, 135426721.933540, 0.191308, 0.680870],
[10, 1241.268649, 135370048.628898, 0.191282, 0.681080],
[11, 1376.739249, 135326524.435675, 0.191248, 0.681345],
[12, 1511.177066, 135292131.796408, 0.191250, 0.681323],
[13, 1642.521336, 135264387.283371, 0.191244, 0.681451],
[14, 1776.739040, 135241643.724179, 0.191265, 0.681452]
]

c_8t = [
[0, 0.195695, 259049122.884103, 0.381797, 0.316477],
[1, 84.235552, 158407956.220849, 0.223583, 0.592351],
[2, 166.181858, 150279699.655933, 0.207375, 0.652110],
[3, 247.176304, 140086323.640911, 0.193055, 0.678176],
[4, 328.177287, 137142722.464173, 0.191627, 0.677318],
[5, 410.376425, 136175463.469850, 0.191565, 0.678365],
[6, 490.923215, 135801789.034298, 0.191509, 0.679023],
[7, 570.291542, 135615396.909001, 0.191436, 0.679817],
[8, 652.268035, 135501371.490557, 0.191353, 0.680166],
[9, 733.451352, 135422935.169475, 0.191326, 0.680516],
[10, 812.709389, 135365443.611906, 0.191301, 0.681093],
[11, 893.113348, 135321573.453930, 0.191303, 0.681171],
[12, 971.779879, 135287054.175775, 0.191303, 0.681215],
[13, 1047.299911, 135259304.074023, 0.191331, 0.681284]
]

w_1c = [
[0, 0.0, 3.927083787114226e8, 0.379201590651579, 0.31671894620514973],
[1, 67.413704292, 1.827411407197719e8, 0.26176860054683676, 0.5596062387904721],
[2, 183.280960369, 1.421663149324522e8, 0.19952644513018827, 0.6618447593979897],
[3, 304.820825061, 1.3786447770573288e8, 0.19421130759272598, 0.6726508207045571],
[4, 426.428635508, 1.3670615206658566e8, 0.192630453724131, 0.6769724317718744],
[5, 545.760992355, 1.3619401602836335e8, 0.191943751262021, 0.6784844595524878],
[6, 665.011704991, 1.3590892059132758e8, 0.1916536264258106, 0.6795708340330294],
[7, 784.375375211, 1.3572858720525923e8, 0.19152472765217657, 0.6803873499076547],
[8, 909.263931941, 1.3560496707110375e8, 0.1914616295511904, 0.6805616030343643],
[9, 1030.962113728, 1.3551544303819266e8, 0.19140140038191392, 0.6806764070300485],
[10, 1149.610516598, 1.3544794483497202e8, 0.19141371247411543, 0.6806877439420751],
[11, 1267.235991885, 1.3539544762121513e8, 0.19141923697712013, 0.6808914617794193]
]

w_4c = [
[0, 0.0, 3.928700598548276e8, 0.3785567430661076, 0.31675573342768726],
[1, 32.487568523, 1.8262888474594197e8, 0.26540599728446973, 0.5777594997594864],
[2, 85.95307364, 1.424376224098723e8, 0.20008067269389807, 0.6624548488237755],
[3, 137.79126025, 1.378902553086152e8, 0.19410960577419129, 0.6734356195565014],
[4, 186.774983241, 1.3670204727094916e8, 0.19245908128822797, 0.6779300352291928],
[5, 234.481393967, 1.361865739560522e8, 0.19180763258475483, 0.6795253250490129],
[6, 281.9509644, 1.3590305015767282e8, 0.19152969530243205, 0.6804976464137378],
[7, 329.847650501, 1.357248156601138e8, 0.1913606587712389, 0.6808695043444382],
[8, 377.093471788, 1.3560279642306435e8, 0.1912769038233849, 0.6810743740565267],
[9, 424.24107938, 1.3551426771435782e8, 0.19122564848715662, 0.6812031853502872],
[10, 471.58265871, 1.3544732753944835e8, 0.19122034817919514, 0.6811970396265483],
[11, 520.836754455, 1.3539513341349393e8, 0.19121351435998069, 0.6813815948112991],
[12, 569.70038691, 1.3535346483819366e8, 0.19122651893667394, 0.6814390503943267],
[13, 618.347906752, 1.353195632197319e8, 0.19123337236830143, 0.6816137798851353],
[14, 667.227347734, 1.3529154783955806e8, 0.19124560395154738, 0.6814887483782239],
[15, 715.351384876, 1.3526808697495875e8, 0.19128297494615462, 0.6813630156842259],
[16, 765.083671818, 1.352482148351559e8, 0.1913129246763375, 0.6812233323042252],
[17, 814.713580847, 1.3523121188410443e8, 0.19129980738494737, 0.6812709118829948],
[18, 865.027767736, 1.3521653377184495e8, 0.19132606939411953, 0.6810301588384892],
[19, 915.368952366, 1.3520376162710676e8, 0.1913375648705414, 0.6810483680372287],
[20, 965.435627563, 1.3519256919222423e8, 0.19135365712142222, 0.6809323596734669]
]


w_8c = [
[0, 0.0, 3.927083787115434e8, 0.379201590651579, 0.31671894620514973],
[1, 24.517270144, 1.8274114071977216e8, 0.26176860054683676, 0.5596062387904721],
[2, 63.624894170000005, 1.4216632395149815e8, 0.19952641897125314, 0.6618418995229471],
[3, 104.003974837, 1.3786447638704646e8, 0.19421096494327014, 0.6726579655633216],
[4, 145.154652576, 1.36706151500047e8, 0.19263023466714893, 0.6769641975898756],
[5, 186.251386191, 1.361940160397203e8, 0.1919437458488466, 0.6784856116335454],
[6, 227.522662448, 1.3590892073410156e8, 0.19165379987541203, 0.679566599316071],
[7, 268.672175018, 1.3572859403020757e8, 0.1915247194843555, 0.6803860519537143],
[8, 309.73053826, 1.356049667007301e8, 0.19146206529344498, 0.6805584626006851],
[9, 350.58882627, 1.355154426992479e8, 0.1914012874639324, 0.6806745800575618],
[10, 390.91924750500004, 1.3544794456669366e8, 0.19141425231540263, 0.6806885294559112],
[11, 430.754662282, 1.3539544739136505e8, 0.1914184301043071, 0.6808931753419623],
[12, 471.25651393600003, 1.3535359229195726e8, 0.1913792113149753, 0.6810044422508016],
[13, 511.44907086700005, 1.3531954250058264e8, 0.19138611070068956, 0.6810462487130993],
[14, 551.975282555, 1.352913755581272e8, 0.19140664841081342, 0.680789049273994],
[15, 591.792691592, 1.3526774757557988e8, 0.1914341545388168, 0.6809571718219022],
[16, 631.908316925, 1.3524768999894398e8, 0.19142329936522914, 0.6808436959524947],
[17, 671.761567764, 1.3523049142641172e8, 0.19145615756763515, 0.6809649477359461],
[18, 712.251646286, 1.3521561255043456e8, 0.19146481585354613, 0.6809692376879046],
[19, 754.000356949, 1.3520264527763522e8, 0.19144538651337517, 0.6809325039069525],
[20, 796.067990366, 1.3519126764581513e8, 0.19144260763048354, 0.6808774149373772]
]

c_4t = np.array(c_4t)
c_8t = np.array(c_8t)
w_1c = np.array(w_1c)
w_4c = np.array(w_4c)
w_8c = np.array(w_8c)

fig, ax = plt.subplots()
ax.plot(w_1c[:,1], w_1c[:,4], 'r--', label='primal 1 core')
ax.plot(w_4c[:,1], w_4c[:,4], 'k-.', label='primal 4 cores')
ax.plot(w_8c[:,1], w_8c[:,4], 'c', label='primal 8 cores')
#ax.plot(c_1t[:,1], c_1t[:,4], 'm:', label='collrank 1 thread')
ax.plot(c_4t[:,1], c_4t[:,4], 'm-.', label='collrank 4 threads')
ax.plot(c_8t[:,1], c_8t[:,4], 'm', label='collrank 8 threads')
ax.set_title('MovieLens10m, 200 ratings/user, rank 100, lambda = 5000')
ax.set_xlabel('Time')
ax.set_ylabel('NDCG')
ax.axis([0, 1000, 0.25, 0.75])
legend = ax.legend(loc='lower right', shadow=True)
frame = legend.get_frame()
frame.set_facecolor('0.90')
plt.show()

fig, ax = plt.subplots()
ax.plot(w_1c[:,1], w_1c[:,3], 'r--', label='primal 1 core')
ax.plot(w_4c[:,1], w_4c[:,3], 'k-.', label='primal 4 cores')
ax.plot(w_8c[:,1], w_8c[:,3], 'c', label='primal 8 cores')
#ax.plot(c_1t[:,1], c_1t[:,3], 'm:', label='collrank 1 thread')
ax.plot(c_4t[:,1], c_4t[:,3], 'm-.', label='collrank 4 threads')
ax.plot(c_8t[:,1], c_8t[:,3], 'm', label='collrank 8 threads')
ax.set_title('MovieLens10m, 200 ratings/user, rank 100, lambda = 7000')
ax.set_xlabel('Time')
ax.set_ylabel('Pairwise_Error')
ax.axis([0, 1000, 0.185, 0.4])
legend = ax.legend(loc='upper right', shadow=True)
frame = legend.get_frame()
frame.set_facecolor('0.90')
plt.show()

fig, ax = plt.subplots()
ax.plot(w_1c[:,1], w_1c[:,2], 'r--', label='primal 1 core')
ax.plot(w_4c[:,1], w_4c[:,2], 'k-.', label='primal 4 cores')
ax.plot(w_8c[:,1], w_8c[:,2], 'c', label='primal 8 cores')
#ax.plot(c_1t[:,1], c_1t[:,2], 'm:', label='collrank 1 thread')
ax.plot(c_4t[:,1], c_4t[:,2], 'm-.', label='collrank 4 threads')
ax.plot(c_8t[:,1], c_8t[:,2], 'm', label='collrank 8 threads')
ax.set_title('MovieLens10m, 200 ratings/user, rank 100, lambda = 7000')
ax.set_xlabel('Time')
ax.set_ylabel('Objective_Function')
ax.axis([0, 1000, 1.3e8, 4.2e8])
legend = ax.legend(loc='upper right', shadow=True)
frame = legend.get_frame()
frame.set_facecolor('0.90')
plt.show()