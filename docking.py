from vina import Vina

receptor = './state000529.pdbqt'
ligand = './ligand-9.pdbqt'
exhaustiveness=32
    
v = Vina(sf_name='vina')
v.set_receptor(receptor)
v.set_ligand_from_file(ligand)
v.compute_vina_maps(center=[52.45, 44.2, 39.51], box_size=[15, 15, 15])
v.dock(exhaustiveness=exhaustiveness)
v.write_poses('ligand-91.pdbqt', n_poses=1)
v.dock(exhaustiveness=exhaustiveness)
v.write_poses('ligand-92.pdbqt', n_poses=1)
