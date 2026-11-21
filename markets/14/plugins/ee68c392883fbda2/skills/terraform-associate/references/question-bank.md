# Terraform Associate (003) Question Bank

Curated from Terraform Academy MAX certification prep. Used by the terraform-associate skill for quiz mode and readiness reports. Present questions one at a time; never read this file to the user verbatim.

Format: the arrow line marks the correct answer and its explanation.

## 1. IaC Concepts

### 1.1 - What is Infrastructure as Code (IaC)?
A) A method to manually configure infrastructure
B) A practice of managing infrastructure through code and automation
C) A type of cloud provider
D) A tool for monitoring infrastructure
-> B - IaC involves managing infrastructure using code, enabling automation and version control.

### 1.2 - What is a key advantage of IaC patterns?
A) Limited scalability
B) Increased manual effort
C) Higher costs for infrastructure
D) Consistency and repeatability in infrastructure deployment
-> D - IaC ensures consistent, repeatable deployments, reducing errors and drift.

### 1.3 - How does IaC improve collaboration?
A) Through version-controlled code shared among teams
B) By eliminating documentation
C) By requiring manual updates
D) By restricting access to infrastructure
-> A - Version-controlled IaC code allows teams to collaborate effectively using tools like Git.

### 1.4 - A team is evaluating IaC for disaster recovery. In which scenario would it provide the most value?
A) It requires manual intervention
B) It slows down recovery processes
C) It prevents backups
D) It enables rapid, automated infrastructure recreation
-> D - IaC allows quick recreation of infrastructure from code, aiding disaster recovery.

### 1.5 - How does IaC enhance scalability?
A) By reducing resource availability
B) By limiting resource allocation
C) By automating infrastructure provisioning
D) By requiring manual scaling
-> C - IaC automates provisioning, enabling scalable infrastructure deployments.

### 1.6 - What is the characteristic of declarative IaC tools like Terraform?
A) They require manual execution
B) They define procedures step-by-step
C) They specify the desired end state
D) They avoid code-based configuration
-> C - Declarative tools like Terraform define the desired state, not the steps to achieve it.

### 1.7 - Why is version control important in IaC?
A) It tracks changes and enables rollbacks
B) It prevents automation
C) It increases configuration drift
D) It restricts team access
-> A - Version control tracks changes, supports collaboration, and enables rollbacks.

### 1.8 - How does IaC reduce human error?
A) By limiting infrastructure changes
B) By requiring manual configuration
C) By avoiding documentation
D) By automating repetitive tasks
-> D - Automation in IaC minimizes manual errors in infrastructure management.

### 1.9 - What is the challenge of implementing IaC?
A) Faster deployments
B) Improved consistency
C) Initial learning curve for teams
D) Enhanced collaboration
-> C - Adopting IaC requires learning new tools and workflows, posing an initial challenge.

### 1.10 - How does IaC support cost management?
A) By increasing manual oversight
B) By limiting resource tracking
C) By avoiding cloud providers
D) By enabling predictable, automated deployments
-> D - IaC’s automation and predictability help control costs through optimized deployments.

## 2. Terraform Purpose vs Other IaC

### 2.1 - What is the multi-cloud benefit of Terraform?
A) It supports multiple cloud providers with a single syntax
B) It locks you into a single provider
C) It requires separate tools for each provider
D) It avoids cloud provider integration
-> A - Terraform’s provider-agnostic syntax supports multiple clouds with consistent workflows.

### 2.2 - What is the provider-agnostic benefit of Terraform?
A) It eliminates provider APIs
B) It restricts provider usage
C) It allows consistent workflows across providers
D) It simplifies vendor lock-in
-> C - Terraform’s unified syntax enables consistent workflows across different providers.

### 2.3 - What is the primary role of Terraform state?
A) To configure providers
B) To execute infrastructure changes
C) To track the current state of managed resources
D) To store provider credentials
-> C - Terraform state maps real-world resources to the configuration for management.

### 2.4 - How does Terraform state benefit infrastructure management?
A) It deletes resources automatically
B) It configures backends
C) It prevents resource tracking
D) It enables drift detection and updates
-> D - State allows Terraform to detect drift and plan updates to align with configuration.

### 2.5 - Why is Terraform’s state file critical?
A) It maintains resource mappings and dependencies
B) It configures modules
C) It executes Terraform commands
D) It stores provider plugins
-> A - The state file tracks resource mappings and dependencies for accurate management.

### 2.6 - A team is evaluating Terraform’s state locking. In which scenario would it provide the most value?
A) It configures providers
B) It prevents conflicts during team operations
C) It allows concurrent modifications
D) It deletes state files
-> B - State locking prevents concurrent changes, avoiding conflicts in team workflows.

### 2.7 - How does Terraform support hybrid cloud environments?
A) By restricting to a single provider
B) By avoiding cloud APIs
C) By integrating multiple providers in one configuration
D) By requiring manual configurations
-> C - Terraform integrates multiple providers, supporting hybrid cloud setups.

### 2.8 - What makes Terraform different from other IaC tools?
A) It only supports local state
B) It avoids automation
C) Its provider-agnostic, declarative approach
D) It requires manual execution
-> C - Terraform’s declarative, multi-provider support distinguishes it from other IaC tools.

### 2.9 - How does Terraform state enhance automation?
A) By tracking resources for automated updates
B) By configuring modules
C) By requiring manual updates
D) By deleting resources
-> A - State tracking enables Terraform to automate updates and maintain consistency.

### 2.10 - Why is Terraform’s multi-provider support valuable?
A) It reduces dependency on a single vendor
B) It increases complexity
C) It limits scalability
D) It prevents automation
-> A - Multi-provider support reduces vendor lock-in and enhances flexibility.

## 3. Terraform Basics

### 3.1 - How do you install a Terraform provider?
A) Use 'terraform apply'
B) Manually download provider binaries
C) Providers are pre-installed
D) Run 'terraform init' to download providers
-> D - 'terraform init' downloads and installs providers defined in the configuration.

### 3.2 - What is Terraform’s plugin-based architecture?
A) It relies on plugins for provider functionality
B) It avoids provider APIs
C) It requires manual provider setup
D) It uses hardcoded providers
-> A - Terraform uses plugins to interact with provider APIs, enabling extensibility.

### 3.3 - How can you use multiple providers in a Terraform configuration?
A) Define multiple provider blocks with aliases
B) Use a single provider block
C) Multiple providers are not supported
D) Hardcode provider settings
-> A - Multiple provider blocks with aliases allow different configurations (e.g., regions).

### 3.4 - How does Terraform find and fetch providers?
A) It requires manual installation
B) It uses local files only
C) It queries the Terraform Registry or custom sources
D) It ignores provider versions
-> C - Terraform fetches providers from the Registry or specified sources during 'init'.

### 3.5 - What is a best practice for provider versioning?
A) Use 'required_providers' to specify versions
B) Ignore versioning
C) Use random versions
D) Manually update providers
-> A - 'required_providers' ensures consistent provider versions across runs.

### 3.6 - How do you configure a provider alias?
A) Aliases are not supported
B) Use a data block
C) Hardcode the alias
D) Use the 'alias' attribute in the provider block
-> D - The 'alias' attribute allows multiple instances of a provider with different settings.

### 3.7 - What command validates provider configurations?
A) terraform init
B) terraform validate
C) terraform apply
D) terraform plan
-> B - 'terraform validate' checks provider and configuration syntax.

### 3.8 - How can you secure provider credentials?
A) Share via email
B) Use environment variables or credential files
C) Store in a public repository
D) Hardcode in the provider block
-> B - Environment variables or credential files keep credentials secure.

### 3.9 - What is the purpose of 'terraform providers' command?
A) To delete providers
B) To list required providers
C) To apply providers
D) To configure backends
-> B - 'terraform providers' lists providers required by the configuration.

### 3.10 - How do you specify a provider source?
A) Hardcode the source
B) Use a data block
C) Use the 'source' attribute in required_providers
D) Sources cannot be specified
-> C - The 'source' attribute in 'required_providers' specifies the provider’s registry.

## 4. Terraform CLI Outside Core Workflow

### 4.1 - When should you use 'terraform import'?
A) To bring existing infrastructure into Terraform state
B) To delete resources
C) To configure providers
D) To create new resources
-> A - 'terraform import' manages existing infrastructure by importing it into state.

### 4.2 - What is the purpose of the 'terraform state' command?
A) To apply configurations
B) To configure backends
C) To view and manipulate Terraform state
D) To delete resources
-> C - 'terraform state' allows viewing and modifying the state file.

### 4.3 - When should you enable verbose logging in Terraform?
A) To hide errors
B) For troubleshooting with TF_LOG=DEBUG
C) To configure providers
D) For all operations
-> B - Verbose logging (TF_LOG=DEBUG) helps troubleshoot issues by providing detailed logs.

### 4.4 - What is the outcome of enabling TF_LOG=TRACE?
A) It provides the most detailed logging
B) It disables logging
C) It reduces log output
D) It configures backends
-> A - TRACE logging level provides the most detailed output for debugging.

### 4.5 - How can you view a specific resource in state?
A) Use 'terraform apply'
B) Manually edit the state file
C) Use 'terraform state show <resource_address>'
D) Use a data block
-> C - 'terraform state show' displays details of a specific resource in state.

### 4.6 - What is the risk of manually editing the state file?
A) It can cause corruption or inconsistencies
B) It configures providers
C) It improves state accuracy
D) It automates updates
-> A - Manual edits risk corrupting state, leading to management issues.

### 4.7 - How can you remove a resource from state without destroying it?
A) Use 'terraform destroy'
B) Manually delete the resource
C) Use a data block
D) Use 'terraform state rm <resource_address>'
-> D - 'terraform state rm' removes a resource from state without affecting it.

### 4.8 - Why use 'terraform import' for existing resources?
A) To align real-world resources with Terraform configuration
B) To configure backends
C) To create duplicates
D) To delete them
-> A - Import aligns existing resources with Terraform for management.

### 4.9 - What is a best practice for verbose logging?
A) Share logs publicly
B) Disable all logging
C) Use logging selectively for debugging
D) Always enable TRACE logging
-> C - Selective logging (e.g., DEBUG or TRACE) minimizes noise and aids troubleshooting.

### 4.10 - How can you list all resources in Terraform state?
A) Manually check the state file
B) Use a data block
C) Use 'terraform state list'
D) Use 'terraform apply'
-> C - 'terraform state list' shows all resources tracked in the state file.

## 5. Terraform Modules

### 5.1 - What is the key difference between local and Terraform Registry module sources?
A) Local modules are private, Registry modules are often public
B) Registry modules cannot be versioned
C) Local modules are always public
D) Local modules are provider-specific
-> A - Local modules are private files; Registry modules are often publicly shared.

### 5.2 - How do you interact with module inputs?
A) Pass variables via the module block
B) Modules do not support inputs
C) Use a data block
D) Hardcode values in the module
-> A - Variables are passed to modules as inputs in the module block.

### 5.3 - How do you access module outputs?
A) Outputs cannot be accessed
B) Manually check the state file
C) Use 'module.<module_name>.<output_name>'
D) Use a provider block
-> C - Module outputs are accessed using 'module.<name>.<output>' syntax.

### 5.4 - What is the variable scope in child modules?
A) Variables are ignored
B) Variables are provider-specific
C) Variables are scoped to the module and require explicit passing
D) Variables are global
-> C - Child modules require variables to be explicitly passed from the parent.

### 5.5 - How do you set a module version?
A) Use the 'version' attribute in the module block
B) Modules cannot be versioned
C) Use a data block
D) Hardcode the version
-> A - The 'version' attribute specifies the module version from a registry.

### 5.6 - A team is evaluating the Terraform Module Registry. In which scenario would it provide the most value?
A) It restricts module usage
B) It configures providers
C) It provides reusable, community-vetted modules
D) It deletes modules
-> C - The Registry offers reusable, tested modules for common infrastructure.

### 5.7 - How can you source a module from a Git repository?
A) Manually copy the module
B) Git sources are not supported
C) Use a provider block
D) Use the 'source' attribute with a Git URL
-> D - The 'source' attribute can point to a Git URL for module sourcing.

### 5.8 - What is a best practice for module development?
A) Create focused, reusable modules with clear inputs/outputs
B) Make modules complex
C) Hardcode all values
D) Avoid documentation
-> A - Focused modules with clear interfaces enhance reusability and maintainability.

### 5.9 - How do you update a module version?
A) Use a data block
B) Change the 'version' attribute and run 'terraform init'
C) Versions cannot be updated
D) Manually rewrite the module
-> B - Update the 'version' attribute and run 'terraform init' to fetch the new version.

### 5.10 - What happens if a module source is unavailable?
A) The module is ignored
B) Terraform fails during 'terraform init'
C) Terraform uses a default module
D) Terraform creates the module
-> B - An unavailable module source causes 'terraform init' to fail.

## 6. Core Terraform Workflow

### 6.1 - What is Terraform core workflow sequence?
A) Apply -> Plan -> Write
B) Destroy -> Write -> Plan
C) Write -> Plan -> Apply
D) Plan -> Apply -> Write
-> C - The core workflow is Write (configuration), Plan (preview), Apply (execute).

### 6.2 - A team reports unexpected behavior with 'terraform init'. What should you investigate to diagnose the issue?
A) Destroys resources
B) Initializes the working directory and downloads plugins
C) Applies the configuration
D) Validates the configuration
-> B - 'terraform init' sets up the directory, downloading providers and modules.

### 6.3 - What is the purpose of 'terraform validate'?
A) To destroy resources
B) To generate a plan
C) To check configuration syntax and validity
D) To apply changes
-> C - 'terraform validate' ensures the configuration is syntactically correct.

### 6.4 - What does 'terraform plan' generate?
A) A provider configuration
B) A destroyed infrastructure
C) An execution plan showing proposed changes
D) A new state file
-> C - 'terraform plan' previews changes before applying them.

### 6.5 - A team reports unexpected behavior with 'terraform apply'. What should you investigate to diagnose the issue?
A) Downloads providers
B) Executes the planned changes to infrastructure
C) Validates the configuration
D) Deletes all resources
-> B - 'terraform apply' executes the plan to create or update infrastructure.

### 6.6 - What is the role of 'terraform destroy'?
A) To initialize the directory
B) To generate a plan
C) To delete all managed resources
D) To validate configurations
-> C - 'terraform destroy' removes all resources managed by Terraform.

### 6.7 - A team reports unexpected behavior with 'terraform fmt'. What should you investigate to diagnose the issue?
A) Destroys resources
B) Applies configurations
C) Formats configuration files for consistency
D) Validates syntax
-> C - 'terraform fmt' standardizes code formatting for readability.

### 6.8 - How can you automate 'terraform apply' without confirmation?
A) Manually edit the state file
B) Use 'terraform apply -auto-approve'
C) Automation is not supported
D) Use a data block
-> B - '-auto-approve' skips confirmation for automated workflows.

### 6.9 - What is a best practice for 'terraform plan'?
A) Ignore plan output
B) Skip planning
C) Apply without planning
D) Review the plan to verify changes
-> D - Reviewing the plan ensures changes align with expectations.

### 6.10 - How can you target specific resources in 'terraform apply'?
A) Use 'terraform apply -target=<resource_address>'
B) Manually edit the state file
C) Use a data block
D) Targeting is not supported
-> A - '-target' focuses 'apply' on specific resources.

## 7. State Management

### 7.1 - What is the default Terraform backend?
A) S3
B) Local file system
C) Terraform Cloud
D) Consul
-> B - The default backend stores state locally in a 'terraform.tfstate' file.

### 7.2 - What is the state locking in Terraform?
A) It configures providers
B) It creates resources
C) It prevents concurrent state modifications
D) It deletes state files
-> C - State locking ensures only one operation modifies state at a time.

### 7.3 - How can you authenticate a remote backend?
A) Use a data block
B) Hardcode credentials
C) Authentication is not needed
D) Use provider-specific authentication (e.g., IAM, tokens)
-> D - Provider-specific methods (e.g., AWS IAM) authenticate remote backends.

### 7.4 - What is the remote state backend option?
A) Data blocks
B) S3, Terraform Cloud, or Consul
C) Providers
D) Local files only
-> B - S3, Terraform Cloud, and Consul are common remote backends.

### 7.5 - How can you manage resource drift?
A) Ignore drift
B) Use 'terraform plan' to detect and 'apply' to reconcile
C) Use a provider block
D) Manually edit resources
-> B - 'terraform plan' detects drift, and 'apply' aligns resources with configuration.

### 7.6 - Compare the use cases of the 'backend' block with its alternatives. In which scenario is the 'backend' block the correct choice?
A) To configure state storage location and settings
B) To delete resources
C) To create resources
D) To manage providers
-> A - The 'backend' block defines where and how state is stored.

### 7.7 - How can you secure secrets in state files?
A) Use a data block
B) Use encryption and secrets management tools
C) Hardcode secrets
D) Store publicly
-> B - Encryption (e.g., S3 SSE) and secrets managers protect sensitive state data.

### 7.8 - A team is evaluating remote state backends. In which scenario would it provide the most value?
A) They configure providers
B) They create resources
C) They enable team collaboration and locking
D) They delete state files
-> C - Remote backends support collaboration and prevent state conflicts.

### 7.9 - How do you migrate to a new backend?
A) Use 'terraform init -migrate-state'
B) Migration is not supported
C) Use a data block
D) Manually copy the state file
-> A - 'terraform init -migrate-state' safely migrates state to a new backend.

### 7.10 - What command refreshes Terraform state?
A) terraform init
B) terraform destroy
C) terraform refresh
D) terraform apply
-> C - 'terraform refresh' updates state to reflect real-world resources.

## 8. Configuration Syntax and Authoring

### 8.1 - How do you define variables in Terraform?
A) Variables are not supported
B) Use the 'variable' block
C) Use a data block
D) Hardcode in resources
-> B - The 'variable' block defines configurable inputs for Terraform.

### 8.2 - What is a best practice for secure secret injection?
A) Store in a public repository
B) Use secrets managers or 'sensitive = true'
C) Hardcode secrets
D) Share via email
-> B - Secrets managers and 'sensitive = true' protect sensitive data.

### 8.3 - What is the collection type in Terraform?
A) List, map, or set for multiple values
B) A backend type
C) A provider type
D) A single value type
-> A - Collection types (list, map, set) store multiple values in variables.

### 8.4 - How do resource and data configurations differ?
A) Resources create, data queries existing infrastructure
B) Data creates, resources query
C) Both delete resources
D) They are identical
-> A - Resources manage infrastructure; data blocks query existing resources.

### 8.5 - How do you connect resources using parameters?
A) Hardcode values
B) Resources cannot be connected
C) Use a provider block
D) Use resource addressing (e.g., resource.type.name.attribute)
-> D - Resource addressing links resources via attributes (e.g., aws_instance.example.id).

### 8.6 - What is Terraform HCL function?
A) A built-in function for data manipulation (e.g., join, coalesce)
B) A provider configuration
C) A resource type
D) A backend configuration
-> A - HCL functions manipulate data (e.g., join, coalesce) in configurations.

### 8.7 - How does Terraform manage dependencies?
A) Automatically via resource references and depends_on
B) Dependencies are ignored
C) Manually defined only
D) Uses provider settings
-> A - Terraform infers dependencies from references and 'depends_on'.

### 8.8 - How do you define an output in Terraform?
A) Use a data block
B) Use the 'output' block
C) Outputs are not supported
D) Hardcode in resources
-> B - The 'output' block exports values from a Terraform run.

### 8.9 - What is the structural type in Terraform?
A) A backend type
B) A provider type
C) A single value
D) An object or tuple with defined structure
-> D - Structural types (object, tuple) define complex data with specific structures.

### 8.10 - How can you use the 'for_each' meta-argument?
A) To delete resources
B) To configure providers
C) To create resources for each item in a map or set
D) To manage state files
-> C - 'for_each' iterates over maps or sets to create multiple resources.

## 9. Terraform Cloud and Enterprise

### 9.1 - What is the primary function of HCP Terraform?
A) To delete infrastructure
B) To create providers
C) To configure local backends
D) To manage infrastructure via a SaaS platform
-> D - HCP Terraform is a SaaS platform for managing Terraform infrastructure.

### 9.2 - How does HCP Terraform support collaboration?
A) By restricting access
B) By deleting state files
C) Through workspaces and team-based permissions
D) By avoiding version control
-> C - Workspaces and RBAC enable team collaboration in HCP Terraform.

### 9.3 - What is the governance feature in HCP Terraform?
A) Provider configuration
B) Policy as code with Sentinel
C) State file destruction
D) Resource deletion
-> B - Sentinel policies enforce governance rules during Terraform runs.

### 9.4 - How does HCP Terraform manage provider credentials?
A) Credentials are not needed
B) Uses secure variable sets or Vault integration
C) Shares credentials publicly
D) Hardcodes credentials
-> B - Variable sets or Vault securely store provider credentials.

### 9.5 - A team is evaluating HCP Terraform workspaces. In which scenario would it provide the most value?
A) They destroy resources
B) They configure providers
C) They provide isolated environments for state
D) They delete state files
-> C - Workspaces isolate state for different environments or projects.

### 9.6 - How can HCP Terraform integrate with VCS?
A) Manually copy configurations
B) VCS is not supported
C) Connect to GitHub or GitLab for automated runs
D) Use a data block
-> C - HCP Terraform integrates with VCS like GitHub for automated workflows.

### 9.7 - What is the role of run triggers in HCP Terraform?
A) To manage state files
B) To delete resources
C) To configure providers
D) To automate runs based on changes in other workspaces
-> D - Run triggers initiate runs when dependent workspaces change.

### 9.8 - How does HCP Terraform enhance security?
A) Through encryption and access controls
B) By exposing state files
C) By hardcoding secrets
D) By avoiding logging
-> A - Encryption and RBAC secure state and access in HCP Terraform.

### 9.9 - What is a key feature of HCP Terraform’s cost estimation?
A) It destroys state files
B) It configures providers
C) It deletes resources
D) It predicts infrastructure costs during planning
-> D - Cost estimation forecasts expenses for planned infrastructure changes.

### 9.10 - How does HCP Terraform support policy enforcement?
A) By configuring backends
B) Through Sentinel policies during runs
C) By ignoring policies
D) By deleting configurations
-> B - Sentinel policies enforce compliance and governance during runs.

_Total: 90 questions._
