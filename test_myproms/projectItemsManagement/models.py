# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AnaComparison(models.Model):
    id_comparison = models.OneToOneField('Comparison', models.DO_NOTHING, db_column='id_comparison', primary_key=True)
    id_analysis = models.ForeignKey('Analysis', models.DO_NOTHING, db_column='id_analysis')
    comp_group = models.SmallIntegerField()
    ana_pos = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ana_comparison'
        unique_together = (('id_comparison', 'id_analysis', 'comp_group'),)


class AnaQuantification(models.Model):
    id_quantification = models.BigIntegerField(primary_key=True)
    id_analysis = models.ForeignKey('Analysis', models.DO_NOTHING, db_column='id_analysis')
    quantif_file = models.CharField(max_length=50, blank=True, null=True)
    is_reference = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ana_quantification'
        unique_together = (('id_quantification', 'id_analysis'),)


class Analysis(models.Model):
    id_analysis = models.BigAutoField(primary_key=True)
    id_sample = models.BigIntegerField()
    name = models.CharField(max_length=100, blank=True, null=True)
    des = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    ms_type = models.CharField(max_length=10, blank=True, null=True)
    instrument = models.CharField(max_length=30, blank=True, null=True)
    data_file = models.CharField(max_length=100, blank=True, null=True)
    file_format = models.CharField(max_length=15, blank=True, null=True)
    wiff_file = models.CharField(max_length=100, blank=True, null=True)
    lab_code = models.CharField(max_length=50, blank=True, null=True)
    labeling = models.CharField(max_length=50, blank=True, null=True)
    decoy = models.CharField(max_length=30, blank=True, null=True)
    false_discovery = models.CharField(max_length=20, blank=True, null=True)
    min_score = models.FloatField(blank=True, null=True)
    max_rank = models.SmallIntegerField(blank=True, null=True)
    taxonomy = models.CharField(max_length=50, blank=True, null=True)
    comments = models.CharField(max_length=250, blank=True, null=True)
    valid_status = models.SmallIntegerField(blank=True, null=True)
    valid_user = models.CharField(max_length=20, blank=True, null=True)
    lower_scores = models.SmallIntegerField(blank=True, null=True)
    verified_mg = models.SmallIntegerField(blank=True, null=True)
    first_valid_date = models.DateTimeField(blank=True, null=True)
    valid_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    display_pos = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'analysis'


class AnalysisDatabank(models.Model):
    id_databank = models.OneToOneField('Databank', models.DO_NOTHING, db_column='id_databank', primary_key=True)
    id_analysis = models.ForeignKey(Analysis, models.DO_NOTHING, db_column='id_analysis')
    db_rank = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'analysis_databank'
        unique_together = (('id_databank', 'id_analysis'),)


class AnalysisModification(models.Model):
    id_analysis = models.OneToOneField(Analysis, models.DO_NOTHING, db_column='id_analysis', primary_key=True)
    id_modification = models.ForeignKey('Modification', models.DO_NOTHING, db_column='id_modification')
    modif_type = models.CharField(max_length=1)
    specificity = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'analysis_modification'
        unique_together = (('id_analysis', 'id_modification', 'modif_type'),)


class AnalysisProtein(models.Model):
    id_analysis = models.OneToOneField(Analysis, models.DO_NOTHING, db_column='id_analysis', primary_key=True)
    id_protein = models.ForeignKey('Protein', models.DO_NOTHING, db_column='id_protein')
    db_rank = models.SmallIntegerField(blank=True, null=True)
    conf_level = models.BigIntegerField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    num_pep = models.BigIntegerField(blank=True, null=True)
    num_match = models.BigIntegerField(blank=True, null=True)
    pep_coverage = models.FloatField(blank=True, null=True)
    match_group = models.BigIntegerField(blank=True, null=True)
    pep_specificity = models.FloatField(blank=True, null=True)
    visibility = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'analysis_protein'
        unique_together = (('id_analysis', 'id_protein'),)


class AnalysisRefrt(models.Model):
    id_reference_rt = models.BigIntegerField(primary_key=True)
    id_analysis = models.ForeignKey(Analysis, models.DO_NOTHING, db_column='id_analysis')
    num_pep = models.BigIntegerField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'analysis_refrt'
        unique_together = (('id_reference_rt', 'id_analysis'),)


class AnalysisSwathLib(models.Model):
    id_swath_lib = models.BigIntegerField(primary_key=True)
    id_analysis = models.ForeignKey(Analysis, models.DO_NOTHING, db_column='id_analysis')
    version_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'analysis_swath_lib'
        unique_together = (('id_swath_lib', 'id_analysis'),)


class AnnotationItem(models.Model):
    id_annotation_item = models.BigAutoField(primary_key=True)
    id_meta_annotation = models.ForeignKey('MetaAnnotation', models.DO_NOTHING, db_column='id_meta_annotation')
    des = models.CharField(max_length=100, blank=True, null=True)
    display_pos = models.SmallIntegerField(blank=True, null=True)
    annot_type = models.CharField(max_length=15, blank=True, null=True)
    annot_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'annotation_item'


class Annotationset(models.Model):
    id_annotationset = models.BigIntegerField(primary_key=True)
    id_exploranalysis = models.ForeignKey('Exploranalysis', models.DO_NOTHING, db_column='id_exploranalysis')
    name = models.CharField(max_length=50, blank=True, null=True)
    rank = models.SmallIntegerField(blank=True, null=True)
    annot_type = models.CharField(max_length=50, blank=True, null=True)
    annot_list = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'annotationset'


class Biosample(models.Model):
    id_biosample = models.BigAutoField(primary_key=True)
    id_species = models.BigIntegerField()
    id_refbiosample = models.ForeignKey('self', models.DO_NOTHING, db_column='id_refbiosample', blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    des = models.CharField(max_length=100, blank=True, null=True)
    is_reference = models.SmallIntegerField(blank=True, null=True)
    record_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'biosample'


class BiosampleProperty(models.Model):
    id_biosample = models.OneToOneField(Biosample, models.DO_NOTHING, db_column='id_biosample', primary_key=True)
    id_property = models.ForeignKey('Property', models.DO_NOTHING, db_column='id_property')
    rank = models.SmallIntegerField(blank=True, null=True)
    property_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'biosample_property'
        unique_together = (('id_biosample', 'id_property'),)


class CatComparison(models.Model):
    id_comparison = models.OneToOneField('Comparison', models.DO_NOTHING, db_column='id_comparison', primary_key=True)
    id_category = models.ForeignKey('Category', models.DO_NOTHING, db_column='id_category')
    comp_group = models.SmallIntegerField(blank=True, null=True)
    cat_pos = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_comparison'
        unique_together = (('id_comparison', 'id_category'),)


class Category(models.Model):
    id_category = models.BigIntegerField(primary_key=True)
    id_classification = models.ForeignKey('Classification', models.DO_NOTHING, db_column='id_classification')
    name = models.CharField(max_length=50, blank=True, null=True)
    des = models.CharField(max_length=100, blank=True, null=True)
    comments = models.CharField(max_length=250, blank=True, null=True)
    list_type = models.CharField(max_length=4, blank=True, null=True)
    display_pos = models.SmallIntegerField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class CategoryProtein(models.Model):
    id_category_protein = models.BigAutoField(primary_key=True)
    id_category = models.ForeignKey(Category, models.DO_NOTHING, db_column='id_category')
    id_protein = models.ForeignKey('Protein', models.DO_NOTHING, db_column='id_protein')

    class Meta:
        managed = False
        db_table = 'category_protein'


class Classification(models.Model):
    id_classification = models.BigIntegerField(primary_key=True)
    id_project = models.ForeignKey('Project', models.DO_NOTHING, db_column='id_project')
    name = models.CharField(max_length=50, blank=True, null=True)
    des = models.CharField(max_length=100, blank=True, null=True)
    comments = models.CharField(max_length=250, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'classification'


class Comparison(models.Model):
    id_comparison = models.BigIntegerField(primary_key=True)
    id_category = models.ForeignKey(Category, models.DO_NOTHING, db_column='id_category', blank=True, null=True)
    id_project = models.ForeignKey('Project', models.DO_NOTHING, db_column='id_project')
    name = models.CharField(max_length=50, blank=True, null=True)
    comments = models.CharField(max_length=250, blank=True, null=True)
    num_groups = models.SmallIntegerField(blank=True, null=True)
    cat_exclusion = models.SmallIntegerField(blank=True, null=True)
    peptide_params = models.TextField(blank=True, null=True)
    sort_order = models.CharField(max_length=15, blank=True, null=True)
    autocheck_params = models.TextField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comparison'


class Databank(models.Model):
    id_databank = models.BigIntegerField(primary_key=True)
    id_dbtype = models.ForeignKey('DatabankType', models.DO_NOTHING, db_column='id_dbtype')
    name = models.CharField(max_length=50, blank=True, null=True)
    version_name = models.CharField(max_length=20, blank=True, null=True)
    des = models.CharField(max_length=100, blank=True, null=True)
    version_date = models.DateField(blank=True, null=True)
    fasta_file = models.CharField(max_length=100, blank=True, null=True)
    num_entry = models.BigIntegerField(blank=True, null=True)
    identifier_type = models.CharField(max_length=50, blank=True, null=True)
    decoy_tag = models.CharField(max_length=100, blank=True, null=True)
    is_crap = models.SmallIntegerField(blank=True, null=True)
    comments = models.CharField(max_length=250, blank=True, null=True)
    use_status = models.CharField(max_length=3, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    organism = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'databank'


class DatabankSwathlib(models.Model):
    id_databank = models.OneToOneField(Databank, models.DO_NOTHING, db_column='id_databank', primary_key=True)
    id_swath_lib = models.BigIntegerField()
    db_rank = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'databank_swathlib'
        unique_together = (('id_databank', 'id_swath_lib'),)


class DatabankType(models.Model):
    id_dbtype = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    des = models.CharField(max_length=100, blank=True, null=True)
    parse_rules = models.CharField(max_length=100, blank=True, null=True)
    def_ident_type = models.CharField(max_length=50, blank=True, null=True)
    ident_mod_string = models.CharField(max_length=30, blank=True, null=True)
    parse_string = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'databank_type'


class Design(models.Model):
    id_design = models.BigIntegerField(primary_key=True)
    id_experiment = models.ForeignKey('Experiment', models.DO_NOTHING, db_column='id_experiment')
    name = models.CharField(max_length=50, blank=True, null=True)
    des = models.CharField(max_length=100, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'design'


class Expcondition(models.Model):
    id_expcondition = models.BigIntegerField(primary_key=True)
    id_design = models.ForeignKey(Design, models.DO_NOTHING, db_column='id_design')
    name = models.CharField(max_length=50, blank=True, null=True)
    des = models.CharField(max_length=100, blank=True, null=True)
    display_pos = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expcondition'


class ExpconditionQuantif(models.Model):
    id_expcondition = models.OneToOneField(Expcondition, models.DO_NOTHING, db_column='id_expcondition', primary_key=True)
    id_quantification = models.BigIntegerField()
    cond_function = models.CharField(max_length=15, blank=True, null=True)
    quantif_element = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expcondition_quantif'
        unique_together = (('id_expcondition', 'id_quantification'),)


class Experiment(models.Model):
    id_experiment = models.BigIntegerField(primary_key=True)
    id_project = models.ForeignKey('Project', models.DO_NOTHING, db_column='id_project')
    id_species = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    des = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    comments = models.CharField(max_length=250, blank=True, null=True)
    display_pos = models.SmallIntegerField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'experiment'


class ExploranaAna(models.Model):
    id_exploranalysis = models.OneToOneField('Exploranalysis', models.DO_NOTHING, db_column='id_exploranalysis', primary_key=True)
    id_analysis = models.ForeignKey(Analysis, models.DO_NOTHING, db_column='id_analysis')
    group_pos = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'explorana_ana'
        unique_together = (('id_exploranalysis', 'id_analysis'),)


class ExploranaQuantif(models.Model):
    id_quantification = models.BigIntegerField(primary_key=True)
    id_exploranalysis = models.ForeignKey('Exploranalysis', models.DO_NOTHING, db_column='id_exploranalysis')
    target_pos = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'explorana_quantif'
        unique_together = (('id_quantification', 'id_exploranalysis', 'target_pos'),)


class Exploranalysis(models.Model):
    id_exploranalysis = models.BigIntegerField(primary_key=True)
    id_category = models.ForeignKey(Category, models.DO_NOTHING, db_column='id_category', blank=True, null=True)
    id_experiment = models.ForeignKey(Experiment, models.DO_NOTHING, db_column='id_experiment')
    name = models.CharField(max_length=50, blank=True, null=True)
    des = models.CharField(max_length=100, blank=True, null=True)
    ana_type = models.CharField(max_length=10, blank=True, null=True)
    param_list = models.TextField(blank=True, null=True)
    filter_list = models.TextField(blank=True, null=True)
    cat_exclusion = models.SmallIntegerField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exploranalysis'


class Gel2D(models.Model):
    id_gel2d = models.BigIntegerField(primary_key=True)
    id_experiment = models.ForeignKey(Experiment, models.DO_NOTHING, db_column='id_experiment')
    name = models.CharField(max_length=50, blank=True, null=True)
    des = models.CharField(max_length=100, blank=True, null=True)
    image_file = models.CharField(max_length=50, blank=True, null=True)
    comments = models.CharField(max_length=250, blank=True, null=True)
    display_pos = models.SmallIntegerField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gel2d'


class GoAnalysis(models.Model):
    id_goanalysis = models.BigAutoField(primary_key=True)
    id_ontology = models.ForeignKey('Ontology', models.DO_NOTHING, db_column='id_ontology')
    id_experiment = models.ForeignKey(Experiment, models.DO_NOTHING, db_column='id_experiment')
    id_goannotation = models.ForeignKey('Goannotation', models.DO_NOTHING, db_column='id_goannotation')
    id_category = models.ForeignKey(Category, models.DO_NOTHING, db_column='id_category', blank=True, null=True)
    id_parent_goana = models.ForeignKey('self', models.DO_NOTHING, db_column='id_parent_goana', blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    des = models.CharField(max_length=100, blank=True, null=True)
    goa_type = models.CharField(max_length=10, blank=True, null=True)
    aspect = models.CharField(max_length=3, blank=True, null=True)
    param_strg = models.TextField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'go_analysis'


class GoanaAnalysis(models.Model):
    id_goanalysis = models.OneToOneField(GoAnalysis, models.DO_NOTHING, db_column='id_goanalysis', primary_key=True)
    id_analysis = models.ForeignKey(Analysis, models.DO_NOTHING, db_column='id_analysis')

    class Meta:
        managed = False
        db_table = 'goana_analysis'
        unique_together = (('id_goanalysis', 'id_analysis'),)


class GoanaQuantification(models.Model):
    id_goanalysis = models.OneToOneField(GoAnalysis, models.DO_NOTHING, db_column='id_goanalysis', primary_key=True)
    id_quantification = models.BigIntegerField()
    ratio = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goana_quantification'
        unique_together = (('id_goanalysis', 'id_quantification'),)


class Goannotation(models.Model):
    id_goannotation = models.BigAutoField(primary_key=True)
    id_species = models.BigIntegerField()
    id_identifier = models.ForeignKey('Identifier', models.DO_NOTHING, db_column='id_identifier', blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    des = models.CharField(max_length=100, blank=True, null=True)
    annot_file = models.CharField(max_length=100, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    version_date = models.DateField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goannotation'


class Identifier(models.Model):
    id_identifier = models.BigIntegerField(primary_key=True)
    id_species = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=15, blank=True, null=True)
    resrc_name = models.CharField(max_length=50, blank=True, null=True)
    resrc_url = models.CharField(max_length=250, blank=True, null=True)
    target = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'identifier'


class Instrument(models.Model):
    id_instrument = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    alias = models.TextField(blank=True, null=True)
    des = models.CharField(max_length=100, blank=True, null=True)
    comments = models.CharField(max_length=250, blank=True, null=True)
    use_status = models.CharField(max_length=3, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    delta_parent = models.CharField(max_length=5, blank=True, null=True)
    delta_fragment = models.CharField(max_length=5, blank=True, null=True)
    tol_fragment = models.FloatField(blank=True, null=True)
    nr_level = models.FloatField(blank=True, null=True)
    rules = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instrument'


class IsotopicCorrection(models.Model):
    id_product = models.BigAutoField(primary_key=True)
    label_type = models.CharField(max_length=15, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    product_number = models.CharField(max_length=25, blank=True, null=True)
    lot_number = models.CharField(max_length=25, blank=True, null=True)
    isotopic_distribution = models.TextField(blank=True, null=True)
    use_status = models.CharField(max_length=3, blank=True, null=True)
    record_date = models.DateTimeField(blank=True, null=True)
    record_user = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'isotopic_correction'


class JobHistory(models.Model):
    id_job = models.CharField(primary_key=True, max_length=50)
    id_project = models.ForeignKey('Project', models.DO_NOTHING, db_column='id_project', blank=True, null=True)
    id_user = models.CharField(max_length=15, blank=True, null=True)
    id_job_cluster = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    features = models.TextField(blank=True, null=True)
    src_path = models.TextField()
    log_path = models.TextField()
    error_path = models.TextField()
    started = models.DateTimeField()
    ended = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_history'


class MasterProtein(models.Model):
    id_master_protein = models.BigAutoField(primary_key=True)
    id_species = models.BigIntegerField(blank=True, null=True)
    prot_des = models.CharField(max_length=250, blank=True, null=True)
    prot_length = models.BigIntegerField(blank=True, null=True)
    mw = models.FloatField(blank=True, null=True)
    prot_seq = models.TextField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_protein'


class MasterprotIdentifier(models.Model):
    id_identifier = models.OneToOneField(Identifier, models.DO_NOTHING, db_column='id_identifier', primary_key=True)
    id_master_protein = models.ForeignKey(MasterProtein, models.DO_NOTHING, db_column='id_master_protein')
    rank = models.SmallIntegerField()
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'masterprot_identifier'
        unique_together = (('id_identifier', 'id_master_protein', 'rank'),)


class MetaAnnotation(models.Model):
    id_meta_annotation = models.BigAutoField(primary_key=True)
    id_parent_annotation = models.ForeignKey('self', models.DO_NOTHING, db_column='id_parent_annotation', blank=True, null=True)
    id_project = models.ForeignKey('Project', models.DO_NOTHING, db_column='id_project')
    id_experiment = models.ForeignKey(Experiment, models.DO_NOTHING, db_column='id_experiment', blank=True, null=True)
    id_sample = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    des = models.CharField(max_length=100, blank=True, null=True)
    display_pos = models.SmallIntegerField(blank=True, null=True)
    accessibility = models.CharField(max_length=10, blank=True, null=True)
    record_date = models.DateTimeField(blank=True, null=True)
    record_user = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta_annotation'


class Modification(models.Model):
    id_modification = models.BigAutoField(primary_key=True)
    unimod_acc = models.BigIntegerField(blank=True, null=True)
    psi_ms_name = models.TextField(blank=True, null=True)
    interim_name = models.CharField(max_length=50, blank=True, null=True)
    des = models.CharField(max_length=100, blank=True, null=True)
    synonymes = models.TextField(blank=True, null=True)
    composition = models.TextField(blank=True, null=True)
    mono_mass = models.FloatField(blank=True, null=True)
    avge_mass = models.FloatField(blank=True, null=True)
    specificity = models.TextField(blank=True, null=True)
    display_code = models.CharField(max_length=5, blank=True, null=True)
    display_color = models.CharField(max_length=7, blank=True, null=True)
    is_subst = models.SmallIntegerField(blank=True, null=True)
    is_label = models.SmallIntegerField(blank=True, null=True)
    peakview_code = models.CharField(max_length=10, blank=True, null=True)
    valid_status = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modification'


class ModificationSite(models.Model):
    id_modification_site = models.BigAutoField(primary_key=True)
    id_modification = models.ForeignKey(Modification, models.DO_NOTHING, db_column='id_modification')
    id_category_protein = models.ForeignKey(CategoryProtein, models.DO_NOTHING, db_column='id_category_protein')
    id_category = models.ForeignKey(Category, models.DO_NOTHING, db_column='id_category')
    residue = models.CharField(max_length=1, blank=True, null=True)
    position = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modification_site'


class ModifiedResidue(models.Model):
    id_modif_res = models.BigAutoField(primary_key=True)
    id_quantification = models.BigIntegerField()
    residue = models.CharField(max_length=1, blank=True, null=True)
    position = models.BigIntegerField(blank=True, null=True)
    modif_rank = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modified_residue'


class MultimodifQuantification(models.Model):
    id_modification = models.OneToOneField(Modification, models.DO_NOTHING, db_column='id_modification', primary_key=True)
    id_quantification = models.BigIntegerField()
    modif_rank = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'multimodif_quantification'
        unique_together = (('id_modification', 'id_quantification'),)


class ObsExpcondition(models.Model):
    id_expcondition = models.OneToOneField(Expcondition, models.DO_NOTHING, db_column='id_expcondition', primary_key=True)
    id_observation = models.ForeignKey('Observation', models.DO_NOTHING, db_column='id_observation')
    fraction_group = models.SmallIntegerField(blank=True, null=True)
    tech_rep_group = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'obs_expcondition'
        unique_together = (('id_expcondition', 'id_observation'),)


class ObsModification(models.Model):
    id_observation = models.OneToOneField('Observation', models.DO_NOTHING, db_column='id_observation', primary_key=True)
    id_modification = models.ForeignKey(Modification, models.DO_NOTHING, db_column='id_modification')

    class Meta:
        managed = False
        db_table = 'obs_modification'
        unique_together = (('id_observation', 'id_modification'),)


class Observation(models.Model):
    id_observation = models.BigAutoField(primary_key=True)
    id_biosample = models.ForeignKey(Biosample, models.DO_NOTHING, db_column='id_biosample', blank=True, null=True)
    id_analysis = models.ForeignKey(Analysis, models.DO_NOTHING, db_column='id_analysis')
    target_pos = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'observation'


class Ontology(models.Model):
    id_ontology = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    obo_file = models.CharField(max_length=100, blank=True, null=True)
    data_version = models.CharField(max_length=15, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    version_date = models.DateField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ontology'


'''class ParentExploranalysis(models.Model):
    id_exploranalysis = models.OneToOneField(Exploranalysis, models.DO_NOTHING, db_column='id_exploranalysis', primary_key=True)
    id_parent_exploranalysis = models.ForeignKey(Exploranalysis, models.DO_NOTHING, db_column='id_parent_exploranalysis')
    display_pos = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parent_exploranalysis'
        unique_together = (('id_exploranalysis', 'id_parent_exploranalysis'),)'''


class ParentQuantification(models.Model):
    id_parent_quantification = models.BigIntegerField(primary_key=True)
    id_quantification = models.BigIntegerField()
    par_function = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parent_quantification'
        unique_together = (('id_parent_quantification', 'id_quantification'),)


class ParentSwathLib(models.Model):
    id_swath_lib = models.BigIntegerField(primary_key=True)
    id_parent_swath_lib = models.BigIntegerField()
    version_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parent_swath_lib'
        unique_together = (('id_swath_lib', 'id_parent_swath_lib'),)


class PathwayAnalysis(models.Model):
    id_pathway_analysis = models.BigAutoField(primary_key=True)
    id_parent_pathwayana = models.ForeignKey('self', models.DO_NOTHING, db_column='id_parent_pathwayana', blank=True, null=True)
    id_experiment = models.ForeignKey(Experiment, models.DO_NOTHING, db_column='id_experiment')
    id_category = models.ForeignKey(Category, models.DO_NOTHING, db_column='id_category', blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    des = models.CharField(max_length=100, blank=True, null=True)
    param_strg = models.TextField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    record_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pathway_analysis'


class PathwayanaAnalysis(models.Model):
    id_analysis = models.OneToOneField(Analysis, models.DO_NOTHING, db_column='id_analysis', primary_key=True)
    id_pathway_analysis = models.ForeignKey(PathwayAnalysis, models.DO_NOTHING, db_column='id_pathway_analysis')

    class Meta:
        managed = False
        db_table = 'pathwayana_analysis'
        unique_together = (('id_analysis', 'id_pathway_analysis'),)


class PathwayanaQuantification(models.Model):
    id_quantification = models.BigIntegerField(primary_key=True)
    id_pathway_analysis = models.ForeignKey(PathwayAnalysis, models.DO_NOTHING, db_column='id_pathway_analysis')
    ratio = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pathwayana_quantification'
        unique_together = (('id_quantification', 'id_pathway_analysis'),)


class Peptide(models.Model):
    id_peptide = models.BigAutoField(primary_key=True)
    id_analysis = models.ForeignKey(Analysis, models.DO_NOTHING, db_column='id_analysis')
    pep_seq = models.CharField(max_length=150, blank=True, null=True)
    pep_length = models.SmallIntegerField(blank=True, null=True)
    query_num = models.BigIntegerField(blank=True, null=True)
    pep_rank = models.SmallIntegerField(blank=True, null=True)
    search_rank = models.SmallIntegerField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    miss_cut = models.SmallIntegerField(blank=True, null=True)
    mr_exp = models.FloatField(blank=True, null=True)
    mr_calc = models.FloatField(blank=True, null=True)
    mr_obs = models.FloatField(blank=True, null=True)
    mr_delta = models.FloatField(blank=True, null=True)
    subst = models.TextField(blank=True, null=True)
    charge = models.SmallIntegerField(blank=True, null=True)
    elution_time = models.CharField(max_length=50, blank=True, null=True)
    valid_status = models.SmallIntegerField(blank=True, null=True)
    comments = models.CharField(max_length=250, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    spec_count = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'peptide'


class PeptideModification(models.Model):
    id_modification = models.OneToOneField(Modification, models.DO_NOTHING, db_column='id_modification', primary_key=True)
    id_peptide = models.ForeignKey(Peptide, models.DO_NOTHING, db_column='id_peptide')
    modif_type = models.CharField(max_length=1)
    pos_string = models.TextField(blank=True, null=True)
    ref_pos_string = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'peptide_modification'
        unique_together = (('id_modification', 'id_peptide'),)


class PeptideProteinAttrib(models.Model):
    id_protein = models.OneToOneField('Protein', models.DO_NOTHING, db_column='id_protein', primary_key=True)
    id_peptide = models.ForeignKey(Peptide, models.DO_NOTHING, db_column='id_peptide')
    id_analysis = models.ForeignKey(Analysis, models.DO_NOTHING, db_column='id_analysis')
    pep_beg = models.BigIntegerField()
    pep_end = models.BigIntegerField(blank=True, null=True)
    flanking_aa = models.CharField(max_length=2, blank=True, null=True)
    is_specific = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'peptide_protein_attrib'
        unique_together = (('id_protein', 'id_peptide', 'pep_beg'),)


class Project(models.Model):
    id_project = models.BigIntegerField(primary_key=True)
    id_identifier = models.ForeignKey(Identifier, models.DO_NOTHING, db_column='id_identifier', blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    des = models.CharField(max_length=100, blank=True, null=True)
    prot_visibility = models.SmallIntegerField(blank=True, null=True)
    owner = models.CharField(max_length=50, blank=True, null=True)
    work_group = models.CharField(max_length=50, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    comments = models.CharField(max_length=250, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    last_open = models.DateTimeField(blank=True, null=True)
    last_user = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project'


class ProjectAccess(models.Model):
    id_user = models.CharField(primary_key=True, max_length=15)
    id_project = models.ForeignKey(Project, models.DO_NOTHING, db_column='id_project')
    id_profile = models.BigIntegerField()
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_access'
        unique_together = (('id_user', 'id_project'),)


class ProjectBiosample(models.Model):
    id_project = models.OneToOneField(Project, models.DO_NOTHING, db_column='id_project', primary_key=True)
    id_biosample = models.ForeignKey(Biosample, models.DO_NOTHING, db_column='id_biosample')

    class Meta:
        managed = False
        db_table = 'project_biosample'
        unique_together = (('id_project', 'id_biosample'),)


class ProjectModification(models.Model):
    id_project = models.OneToOneField(Project, models.DO_NOTHING, db_column='id_project', primary_key=True)
    id_modification = models.ForeignKey(Modification, models.DO_NOTHING, db_column='id_modification')

    class Meta:
        managed = False
        db_table = 'project_modification'
        unique_together = (('id_project', 'id_modification'),)


class ProjectProperty(models.Model):
    id_project = models.OneToOneField(Project, models.DO_NOTHING, db_column='id_project', primary_key=True)
    id_property = models.ForeignKey('Property', models.DO_NOTHING, db_column='id_property')

    class Meta:
        managed = False
        db_table = 'project_property'
        unique_together = (('id_project', 'id_property'),)


class Property(models.Model):
    id_property = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    des = models.CharField(max_length=100, blank=True, null=True)
    property_type = models.CharField(max_length=1, blank=True, null=True)
    possible_values = models.TextField(blank=True, null=True)
    use_in_analysis = models.SmallIntegerField(blank=True, null=True)
    is_verified = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'property'


class Protein(models.Model):
    id_protein = models.BigAutoField(primary_key=True)
    id_project = models.ForeignKey(Project, models.DO_NOTHING, db_column='id_project')
    id_master_protein = models.ForeignKey(MasterProtein, models.DO_NOTHING, db_column='id_master_protein', blank=True, null=True)
    alias = models.CharField(max_length=50, blank=True, null=True)
    identifier = models.CharField(max_length=50, blank=True, null=True)
    prot_des = models.CharField(max_length=250, blank=True, null=True)
    prot_length = models.BigIntegerField(blank=True, null=True)
    prot_seq = models.TextField(blank=True, null=True)
    mw = models.FloatField(blank=True, null=True)
    organism = models.CharField(max_length=100, blank=True, null=True)
    comments = models.CharField(max_length=250, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'protein'


class ProteinQuantification(models.Model):
    id_prot_quantif = models.BigAutoField(primary_key=True)
    id_protein = models.ForeignKey(Protein, models.DO_NOTHING, db_column='id_protein')
    id_quantification = models.BigIntegerField()
    id_quantif_parameter = models.BigIntegerField()
    quantif_value = models.FloatField(blank=True, null=True)
    target_pos = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'protein_quantification'
