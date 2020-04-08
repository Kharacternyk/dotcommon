from dotcommon.count_atoms import count_atoms

def process_preset(repos, preset, output):
    output.wite_preset(preset)   
    succeeded, counters_atomizers = count_atoms(repos, *preset.preset)
    output.echo(succeeded, "configs were found.")
    for counter, atomizer in counters_atomizers:
        output.write_atomizer(atomizer)
        output.write_counter(counter)


