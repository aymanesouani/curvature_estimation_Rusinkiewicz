import trimesh
import numpy as np
import CalculCurvature as CC

if __name__ == '__main__':
	
	# Generate a sphere
	mesh = trimesh.creation.icosphere()
	
	# Show th sphere
	mesh.show()
	
	# Calculate Rusinkiewicz estimation of mean and gauss curvatures
	PrincipalCurvatures, PrincipalDir1, PrincipalDir2 = CC.GetCurvaturesAndDerivatives(mesh)
	gaussian_curv = PrincipalCurvatures[0, :] * PrincipalCurvatures[1, :]
	mean_curv = 0.5 * (PrincipalCurvatures[0, :] + PrincipalCurvatures[1, :])
	
	# Plot mean curvature
	vect_col_map = \
		trimesh.visual.color.interpolate(mean_curv, color_map='jet')
	
	if mean_curv.shape[0] == mesh.vertices.shape[0]:
		mesh.visual.vertex_colors = vect_col_map
	elif mean_curv.shape[0] == mesh.faces.shape[0]:
		mesh.visual.face_colors = vect_col_map
	mesh.show( background=[0, 0, 0, 255])
	
	# PLot Gauss curvature
	vect_col_map = \
		trimesh.visual.color.interpolate(gaussian_curv, color_map='jet')
	if gaussian_curv.shape[0] == mesh.vertices.shape[0]:
		mesh.visual.vertex_colors = vect_col_map
	elif gaussian_curv.shape[0] == mesh.faces.shape[0]:
		mesh.visual.face_colors = vect_col_map
	mesh.show(background=[0, 0, 0, 255])
	
	# Calculate mean error between real and estimated curvatures

	#Mean curvature

	mesh_coords = mesh.vertices
	curv_mean_real = gqs.quadric_curv_mean(Ks[0][0], Ks[0][1])(mesh_coords[:, 0], mesh_coords[:, 1])
	print("Error = ", np.mean(np.abs(mean_curv - curv_mean_real)))

	#Gauss curvature
	
	curv_gauss_real = gqs.quadric_curv_gauss(Ks[0][0], Ks[0][1])(mesh_coords[:, 0], mesh_coords[:, 1])
	print("Error = ", np.mean(np.abs(gaussian_curv - curv_gauss_real)))
