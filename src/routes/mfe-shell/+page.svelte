<script lang="ts">
</script>

<svelte:head>
	<title>Micro-Frontend Shell Development | Code Pasture</title>
	<meta
		name="description"
		content="Break free from frontend monoliths. Code Pasture builds Svelte 5 MFE shells with native ES modules, enabling team autonomy and independent deployability."
	/>
	<meta property="og:title" content="Micro-Frontend Shell Development" />
	<meta
		property="og:description"
		content="Break free from frontend monoliths. Svelte 5 MFE shells with native ES modules, team autonomy, and independent deployability."
	/>
	<meta property="og:image" content="https://codepasture.com/mfe-shell-logo.png" />
	<meta property="og:url" content="https://codepasture.com/mfe-shell/" />
	<meta property="og:type" content="website" />
</svelte:head>

<div class="page">
	<header class="page-header">
		<a href="/" class="back-link">&larr; Code Pasture</a>
	</header>

	<main class="content">
		<section class="hero">
			<h1>Micro-Frontend Shell Development</h1>
			<p class="tagline">Break free from frontend monoliths. Ship independently. Scale your teams.</p>
			<div class="hero-actions">
				<a href="#discovery" class="btn-primary">Start Discovery</a>
				<a href="https://nathanfox.net" class="btn-secondary" target="_blank" rel="noopener"
					>Read the Blog</a
				>
			</div>
		</section>

		<section class="section">
			<h2>The Problem</h2>
			<p>
				Your frontend has become a monolith. Different teams work on the same codebase, deployments
				require coordination across the organization, and a bug in one feature can bring down
				everything.
			</p>
			<p>
				We fought monoliths on the backend for years and won with microservices. Yet on the
				frontend, we keep building massive single-page applications where every team commits to the
				same repo and every feature ships together.
			</p>
			<p>It's time to apply the same principles to your frontend.</p>
		</section>

		<section class="section">
			<h2>The Solution</h2>
			<div class="features-grid">
				<div class="feature">
					<h3>Independent Deployability</h3>
					<p>
						Ship features on your own schedule. No more waiting for the quarterly release train or
						coordinating deployments across teams.
					</p>
				</div>
				<div class="feature">
					<h3>Clear Ownership</h3>
					<p>
						Each team owns their vertical slice: frontend MFE and backend microservice together. The
						same repo, the same team, the same deployment pipeline.
					</p>
				</div>
				<div class="feature">
					<h3>Technology Flexibility</h3>
					<p>
						The architecture supports any framework—React, Vue, Angular, Svelte, SolidJS—though we
						recommend standardizing where possible.
					</p>
				</div>
				<div class="feature">
					<h3>Team Autonomy</h3>
					<p>
						Self-contained teams make their own decisions without blocking on shared code. No more
						debates about which service owns what functionality.
					</p>
				</div>
				<div class="feature">
					<h3>Fault Isolation</h3>
					<p>
						A bug in one MFE doesn't crash the others. Problems stay contained within bounded
						contexts.
					</p>
				</div>
				<div class="feature">
					<h3>GenAI-Friendly</h3>
					<p>
						Smaller, focused codebases are ideal for AI-assisted development. Cleaner context
						windows, better pattern recognition, faster iteration.
					</p>
				</div>
			</div>
		</section>

		<section class="section why-svelte">
			<h2>Why Svelte 5 for the Shell</h2>
			<div class="comparison">
				<div class="stat">
					<span class="stat-value">~2 KB</span>
					<span class="stat-label">Svelte 5 runtime</span>
				</div>
				<div class="stat-divider">vs</div>
				<div class="stat">
					<span class="stat-value">40+ KB</span>
					<span class="stat-label">React runtime</span>
				</div>
			</div>
			<p class="comparison-note">The shell runs on every page load. Size matters.</p>
			<ul class="benefits-list">
				<li>
					<strong>Compiles away:</strong> Svelte becomes vanilla JavaScript—no framework conflicts with
					your MFEs regardless of what framework they use.
				</li>
				<li>
					<strong>Native ES Modules:</strong> No Webpack Module Federation required. Standard browser
					imports that are future-proof.
				</li>
				<li>
					<strong>Minimal footprint:</strong> The shell should be invisible infrastructure. Svelte makes
					it nearly so.
				</li>
				<li>
					<strong>Battle-tested:</strong> Production deployments in 5 days. Real teams shipping real features.
				</li>
			</ul>
		</section>

		<section id="discovery" class="section">
			<h2>Discovery Process</h2>
			<p class="section-intro">
				Every MFE implementation starts with understanding your current state. Here's what we
				evaluate together:
			</p>
			<div class="discovery-grid">
				<div class="discovery-item">
					<h3>Authentication & Authorization</h3>
					<ul>
						<li>Current auth provider (OAuth, SAML, custom)</li>
						<li>Token management strategy</li>
						<li>Role-based access requirements</li>
						<li>Cross-MFE auth state sharing</li>
					</ul>
				</div>
				<div class="discovery-item">
					<h3>Existing UI Stack</h3>
					<ul>
						<li>Current frameworks (React, Vue, Angular, etc.)</li>
						<li>Component libraries in use</li>
						<li>State management patterns</li>
						<li>Build tooling and bundlers</li>
					</ul>
				</div>
				<div class="discovery-item">
					<h3>Theming & Design System</h3>
					<ul>
						<li>Existing design tokens</li>
						<li>CSS methodology (Tailwind, CSS Modules, etc.)</li>
						<li>Dark/light mode requirements</li>
						<li>Component style isolation needs</li>
					</ul>
				</div>
				<div class="discovery-item">
					<h3>CI/CD Pipeline</h3>
					<ul>
						<li>Current pipeline platform</li>
						<li>Deployment frequency goals</li>
						<li>Testing automation maturity</li>
						<li>Environment strategy (dev, staging, prod)</li>
					</ul>
				</div>
				<div class="discovery-item">
					<h3>Hosting & Infrastructure</h3>
					<ul>
						<li>Current hosting platform</li>
						<li>Container orchestration (Kubernetes preferred)</li>
						<li>CDN and edge requirements</li>
						<li>Multi-region considerations</li>
					</ul>
				</div>
				<div class="discovery-item">
					<h3>Team Structure</h3>
					<ul>
						<li>Number of frontend teams</li>
						<li>Current deployment coordination pain</li>
						<li>Desired autonomy level</li>
						<li>Shared services vs. team ownership</li>
					</ul>
				</div>
			</div>
		</section>

		<section class="section">
			<h2>How We Work</h2>
			<div class="process-steps">
				<div class="step">
					<span class="step-number">1</span>
					<div class="step-content">
						<h3>Discovery Call</h3>
						<p>1-hour conversation to understand your architecture, pain points, and goals.</p>
					</div>
				</div>
				<div class="step">
					<span class="step-number">2</span>
					<div class="step-content">
						<h3>Architecture Assessment</h3>
						<p>
							Deep dive into your codebase. We document the current state and propose an MFE
							migration path.
						</p>
					</div>
				</div>
				<div class="step">
					<span class="step-number">3</span>
					<div class="step-content">
						<h3>Shell Development</h3>
						<p>
							We build your Svelte 5 MFE shell, configured for your auth, theming, and routing
							needs.
						</p>
					</div>
				</div>
				<div class="step">
					<span class="step-number">4</span>
					<div class="step-content">
						<h3>First MFE</h3>
						<p>We build a working example or migrate an existing feature to prove the pattern. Your team learns the approach.</p>
					</div>
				</div>
				<div class="step">
					<span class="step-number">5</span>
					<div class="step-content">
						<h3>Team Enablement</h3>
						<p>Documentation, training, and handoff. Your teams can create new MFEs independently.</p>
					</div>
				</div>
			</div>
		</section>

		<section class="section cta">
			<h2>Ready to Break Free?</h2>
			<p>
				Let's discuss whether micro-frontends are right for your organization. No obligation, no
				sales pitch—just a technical conversation.
			</p>
			<a href="mailto:contact@codepasture.com?subject=MFE%20Shell%20Discovery" class="cta-link"
				>Schedule a Discovery Call &rarr;</a
			>
		</section>

		<section class="section">
			<p class="footer-links">
				<a href="/">← Back to Code Pasture</a> &middot;
				<a
					href="https://github.com/nathanfox/mfe-svelte-shell-example"
					target="_blank"
					rel="noopener">View Example on GitHub</a
				>
			</p>
		</section>
	</main>
</div>

<style>
	.page {
		min-height: 100vh;
		padding: 2rem;
		max-width: 900px;
		margin: 0 auto;
	}

	.page-header {
		margin-bottom: 3rem;
	}

	.back-link {
		color: var(--color-text-muted);
		font-size: 0.9rem;
	}

	.back-link:hover {
		color: var(--color-accent);
	}

	.hero {
		text-align: center;
		margin-bottom: 4rem;
	}

	.hero h1 {
		font-size: 2.5rem;
		font-weight: 700;
		margin-bottom: 0.75rem;
	}

	.tagline {
		font-size: 1.25rem;
		color: var(--color-text-muted);
		margin-bottom: 2rem;
	}

	.hero-actions {
		display: flex;
		justify-content: center;
		gap: 1rem;
		flex-wrap: wrap;
	}

	.btn-primary {
		padding: 0.75rem 1.5rem;
		background: var(--color-accent);
		color: var(--color-bg);
		font-weight: 600;
		border-radius: var(--radius-md);
		transition: opacity var(--transition-fast);
	}

	.btn-primary:hover {
		opacity: 0.9;
	}

	.btn-secondary {
		padding: 0.75rem 1.5rem;
		background: transparent;
		color: var(--color-text);
		font-weight: 600;
		border: 1px solid var(--color-border);
		border-radius: var(--radius-md);
		transition:
			border-color var(--transition-fast),
			color var(--transition-fast);
	}

	.btn-secondary:hover {
		border-color: var(--color-accent);
		color: var(--color-accent);
	}

	.section {
		margin-bottom: 3rem;
	}

	.section h2 {
		font-size: 1.5rem;
		font-weight: 600;
		margin-bottom: 1rem;
		color: var(--color-accent);
	}

	.section p {
		color: var(--color-text-muted);
		line-height: 1.8;
		margin-bottom: 1rem;
	}

	.section-intro {
		margin-bottom: 1.5rem;
	}

	.features-grid {
		display: grid;
		grid-template-columns: repeat(2, 1fr);
		gap: 1.5rem;
	}

	.feature {
		padding: 1.5rem;
		background: var(--color-bg-elevated);
		border: 1px solid var(--color-border);
		border-radius: var(--radius-md);
	}

	.feature h3 {
		font-size: 1rem;
		font-weight: 600;
		margin-bottom: 0.5rem;
		color: var(--color-text);
	}

	.feature p {
		font-size: 0.9rem;
		margin: 0;
	}

	/* Why Svelte section */
	.comparison {
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 2rem;
		margin: 2rem 0;
		padding: 2rem;
		background: var(--color-bg-elevated);
		border: 1px solid var(--color-border);
		border-radius: var(--radius-md);
	}

	.stat {
		text-align: center;
	}

	.stat-value {
		display: block;
		font-family: var(--font-mono);
		font-size: 2rem;
		font-weight: 700;
		color: var(--color-accent);
	}

	.stat-label {
		display: block;
		font-size: 0.85rem;
		color: var(--color-text-muted);
		margin-top: 0.25rem;
	}

	.stat-divider {
		font-size: 1.25rem;
		color: var(--color-text-muted);
		font-weight: 500;
	}

	.comparison-note {
		text-align: center;
		font-style: italic;
	}

	.benefits-list {
		list-style: none;
		padding: 0;
		margin: 1.5rem 0 0 0;
	}

	.benefits-list li {
		padding: 0.75rem 0;
		border-bottom: 1px solid var(--color-border);
		color: var(--color-text-muted);
		line-height: 1.6;
	}

	.benefits-list li:last-child {
		border-bottom: none;
	}

	.benefits-list strong {
		color: var(--color-text);
	}

	/* Discovery grid */
	.discovery-grid {
		display: grid;
		grid-template-columns: repeat(2, 1fr);
		gap: 1.5rem;
	}

	.discovery-item {
		padding: 1.5rem;
		background: var(--color-bg-elevated);
		border: 1px solid var(--color-border);
		border-radius: var(--radius-md);
	}

	.discovery-item h3 {
		font-size: 1rem;
		font-weight: 600;
		margin-bottom: 0.75rem;
		color: var(--color-text);
	}

	.discovery-item ul {
		list-style: none;
		padding: 0;
		margin: 0;
	}

	.discovery-item li {
		font-size: 0.85rem;
		color: var(--color-text-muted);
		padding: 0.25rem 0;
		padding-left: 1rem;
		position: relative;
	}

	.discovery-item li::before {
		content: '•';
		position: absolute;
		left: 0;
		color: var(--color-accent);
	}

	/* Process steps */
	.process-steps {
		display: flex;
		flex-direction: column;
		gap: 1rem;
	}

	.step {
		display: flex;
		gap: 1rem;
		padding: 1.25rem;
		background: var(--color-bg-elevated);
		border: 1px solid var(--color-border);
		border-radius: var(--radius-md);
		align-items: flex-start;
	}

	.step-number {
		flex-shrink: 0;
		width: 2rem;
		height: 2rem;
		display: flex;
		align-items: center;
		justify-content: center;
		background: var(--color-accent);
		color: var(--color-bg);
		font-weight: 700;
		border-radius: 50%;
		font-size: 0.9rem;
	}

	.step-content h3 {
		font-size: 1rem;
		font-weight: 600;
		margin-bottom: 0.25rem;
		color: var(--color-text);
	}

	.step-content p {
		font-size: 0.9rem;
		margin: 0;
	}

	/* CTA */
	.cta {
		background: var(--color-bg-elevated);
		border: 1px solid var(--color-border);
		border-radius: var(--radius-lg);
		padding: 2rem;
		text-align: center;
	}

	.cta h2 {
		color: var(--color-text);
	}

	.cta-link {
		display: inline-block;
		margin-top: 1rem;
		padding: 0.75rem 1.5rem;
		background: var(--color-accent);
		color: var(--color-bg);
		font-weight: 600;
		border-radius: var(--radius-md);
		transition: opacity var(--transition-fast);
	}

	.cta-link:hover {
		opacity: 0.9;
	}

	.footer-links {
		padding-top: 2rem;
		border-top: 1px solid var(--color-border);
		text-align: center;
	}

	@media (max-width: 768px) {
		.page {
			padding: 1.5rem;
		}

		.hero h1 {
			font-size: 1.75rem;
		}

		.tagline {
			font-size: 1rem;
		}

		.features-grid,
		.discovery-grid {
			grid-template-columns: 1fr;
		}

		.comparison {
			flex-direction: column;
			gap: 1rem;
		}

		.stat-divider {
			display: none;
		}

		.section h2 {
			font-size: 1.25rem;
		}
	}
</style>
