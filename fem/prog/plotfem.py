# data
coord = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/fem/uh_square.csv',header=None).values
x = coord[:,0]
y = coord[:,1]
z = coord[:,2]
tridata = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/fem/Th_square.csv',header=None).values
tri = mtri.Triangulation(x,y,triangles=tridata)

# plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(tri,z,cmap=plt.cm.jet)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.view_init(elev=30, azim=-60)
plt.savefig('/content/drive/MyDrive/Colab Notebooks/fem/uh_square.png',dpi=300, bbox_inches='tight')
plt.show()
